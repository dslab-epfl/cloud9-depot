# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A thread pool implementation used by the Google Compute Engine library."""

import collections
import Queue
import threading
import time


class TokenBucket(object):
  """Implements the token bucket algorithm.

  TokenBucket allows clients to perform a set of actions while
  conforming to a rate limit. This class is thread safe.

  Example usage:

    tk = TokenBucket(capacity=10, rate=1)
    # ...
    while not tk.get_token():
      # Wait for more tokens to be added to the bucket.
      time.sleep(0.5)
    do_something()
  """

  def __init__(self, capacity, rate, timer=None):
    """Creates a new TokenBucket.

    Args:
      capacity: The maximum number of tokens the bucket should hold.
      rate: The rate at which new tokens should be added to the bucket
        in tokens/second.
      timer: A function that returns the current time in seconds. This
        is used for testing.
    """
    self._capacity = capacity
    self._num_tokens = capacity
    self._rate = rate
    self._lock = threading.Lock()
    self._time = timer or time.time
    self._last_time = self._time()

  def get_token(self):
    """Returns True if a token is available.

    If this method returns True, one token is removed from the bucket.

    Returns:
      True when a token is available.
    """
    self._lock.acquire()

    # Updates the number of tokens in the bucket.
    now = self._time()
    self._num_tokens += (now - self._last_time) * self._rate
    self._num_tokens = min(self._num_tokens, self._capacity)
    self._last_time = now

    has_token = False
    if self._num_tokens >= 1:
      self._num_tokens -= 1
      has_token = True
    self._lock.release()
    return has_token


class Future(object):
  """Facilitates the passing of results from asynchronous operations."""

  __NO_RES = object()

  def __init__(self):
    """Constructs a new Future."""
    self._lock = threading.Lock()
    self._lock.acquire()
    self._result = Future.__NO_RES

  def _set_result(self, result):
    """Sets the return value for the operation.

    Once the result is set, wait() will unblock.

    Raises:
      ValueError: If a result has already been registered with
        this Future.

    Args:
      result: The result to associate with this Future.
    """
    if self._result is not Future.__NO_RES:
      raise ValueError('The result can only be set once.')

    self._result = result
    self._lock.release()

  def wait(self):
    """Blocks until the result is available.

    Returns:
      The result.
    """
    self._lock.acquire()
    return self._result


class ThreadPool(object):
  """A simple thread pool implementation that enforces rate limiting.

  Example usage:

    def my_function(x, y):
      return x * y

    pool = ThreadPool(num_threads=10, rate=1)
    pool.start()
    future = pool.submit(my_function, 3, y=2)
    assert future.wait() == 6
    pool.join()
  """
  # A unit of work.
  _Work = collections.namedtuple('Work', ['future', 'func', 'args', 'kwargs'])

  # States
  _INIT = 0
  _RUNNING = 1
  _TERMINATING = 2
  _TERMINATED = 3

  def __init__(self, num_threads, rate):
    """Constructs a new ThreadPool.

    Args:
      num_threads: The number of threads in the pool.
      rate: The rate at which jobs will be invoked in jobs/second.
    """
    self._queue = Queue.Queue()
    self._token_bucket = TokenBucket(num_threads, rate)
    self._num_threads = num_threads
    self._threads = None
    self._state = self._INIT

  def start(self):
    """Starts the thread pool.

    Raises:
      ValueError: If the thread pool has already been started.
    """
    if self._state != ThreadPool._INIT:
      raise ValueError('The thread pool has already been started.')

    self._threads = []
    for _ in xrange(self._num_threads):
      thread = threading.Thread(target=self._worker)
      thread.setDaemon(True)
      self._threads.append(thread)
      thread.start()
    self._state = ThreadPool._RUNNING

  def submit(self, func, *args, **kwargs):
    """Submits a new job to the pool.

    Args:
      func: The function to execute.
      *args: The positional arguments to func.
      **kwargs: The key-word arguments to func.

    Raises:
      ValueError: If the thread pool is not running.

    Returns:
      A future that will contain the function's return value once the
      job is executed.
    """
    if self._state != ThreadPool._RUNNING:
      raise ValueError('The thread pool is not currently running.')

    future = Future()
    work = ThreadPool._Work(future, func, args, kwargs)
    self._queue.put(work)
    return future

  def _worker(self):
    """The main thread that each worker thread runs."""
    while True:
      work = self._queue.get()
      if work is None:
        return

      while not self._token_bucket.get_token():
        time.sleep(0.5)

      try:
        res = work.func(*work.args, **work.kwargs)
      except BaseException as e:
        res = e

      work.future._set_result(res)
      self._queue.task_done()

  def join(self):
    """Causes the thread pool to shutdown.

    Raises:
      ValueError: The thread pool is not currently running.
    """

    if self._state != ThreadPool._RUNNING:
      raise ValueError('The thread pool is not running.')

    self._state = ThreadPool._TERMINATING

    for _ in self._threads:
      self._queue.put(None)

    for thread in self._threads:
      thread.join()

    self._state = ThreadPool._TERMINATED
