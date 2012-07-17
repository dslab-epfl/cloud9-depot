#!/usr/bin/python
#
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

"""Tests for the thread_pool module."""

import unittest

import thread_pool


class TokenBucketTests(unittest.TestCase):
  """Tests the TokenBucket."""

  def setUp(self):
    self._time = 0

  def time(self):
    """A mock time function meant to replace time.time()."""
    self._time += 1
    return self._time

  def test_get_token(self):
    tb = thread_pool.TokenBucket(capacity=5, rate=0.3, timer=self.time)
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())

    self._time = 0
    tb = thread_pool.TokenBucket(capacity=2, rate=0.5, timer=self.time)
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())

    self._time = 0
    tb = thread_pool.TokenBucket(capacity=10, rate=0.5, timer=self.time)
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())
    self.assertFalse(tb.get_token())
    self.assertTrue(tb.get_token())


class FutureTests(unittest.TestCase):
  """Tests the Future class."""

  def test_edge_cases(self):
    future = thread_pool.Future()
    future._set_result(None)

    future = thread_pool.Future()
    future._set_result(42)
    try:
      future._set_result(43)
      self.fail()
    except ValueError:
      pass

  def test_wait(self):
    future = thread_pool.Future()
    future._set_result(42)
    self.assertEqual(future.wait(), 42)


class ThreadPoolTests(unittest.TestCase):
  """Tests for ThreadPool."""

  def test_basic(self):
    """Ensures that the thread pool maintains consistent state."""
    tp = thread_pool.ThreadPool(5, 10)
    tp.start()
    tp.join()

    tp = thread_pool.ThreadPool(5, 10)
    self.assertRaises(ValueError, tp.join)
    tp.start()
    tp.join()
    self.assertRaises(ValueError, tp.start)

    tp = thread_pool.ThreadPool(5, 10)
    tp.start()
    self.assertRaises(ValueError, tp.start)
    self.assertRaises(ValueError, tp.start)
    tp.join()
    self.assertRaises(ValueError, tp.join)
    self.assertRaises(ValueError, tp.join)

    tp = thread_pool.ThreadPool(5, 10)
    self.assertRaises(ValueError, tp.submit, self.fail)

  def test_submit(self):
    """Ensures that tasks can be submitted to the pool."""

    def work_fn():
      return 42

    tp = thread_pool.ThreadPool(1, 10)
    tp.start()
    future = tp.submit(work_fn)
    self.assertEqual(future.wait(), 42)
    tp.join()

    num_threads = 100
    futures = []
    tp = thread_pool.ThreadPool(num_threads, 10)
    tp.start()
    for _ in range(num_threads):
      futures.append(tp.submit(work_fn))
    for future in futures:
      self.assertEqual(future.wait(), 42)
    tp.join()


if __name__ == '__main__':
  unittest.main()
