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

"""The base class definition for the generated GoogleComputeEngine class."""

import collections
import itertools
import json
import logging
import re
import thread_pool
import time
import urllib
import urlparse

import httplib2
import shortcuts

LOG_FORMAT = '{start_bold}%(asctime)s{reset_colors} - %(message)s'.format(
    start_bold='\033[1m', reset_colors='\033[0m')
BASE_URL_TEMPLATE = 'https://www.googleapis.com/compute/{0}/projects/'
DEFAULT_BASE_URL = BASE_URL_TEMPLATE.format('v1beta12')

# The maximum amount of time that should be spent polling an Operation
# object before giving up.
TIMEOUT_SECS = 60

# Thread pool parameters.
THREAD_COUNT = 5
RATE_LIMIT = 20

class GoogleComputeEngineBase(object):
  """The base class from which the generated code derives."""

  _SELF_LINK_REGEX = re.compile(
      'https?://[^/]+/compute/[^/]+/projects/([^/]+)(?:/.*)?')

  API_REQUEST = collections.namedtuple(
      'ApiRequest', ('method', 'url', 'query', 'body'))

  def __init__(self, credentials,
               logging_level=logging.WARN,
               base_url=None,
               default_image=None,
               default_machine_type=None,
               default_network='default',
               default_network_interface=None,
               default_project=None,
               default_zone=None):
    """Base class constructor.

    Args:
      credentials: A OAuth2Credentials object that contains the
        client's credentials.
      logging_level: The verbosity of the log messages as defined
        in the logging module.
      base_url: The base URL to which REST requests can be made. This
        should not be changed.
      default_image: The name of the default image. This value can be
        overwritten by the different API calls.
      default_machine_type: The name of the default machine type. This
        value can be overwritten by the different API calls.
      default_network: The default network. This value can be overwritten
        by the different API calls.
      default_network_interface: The default network interface. This
        value can be overwritten by the different API calls.
      default_project: The name of the default project. This value can
        be overwritten by the different API calls.
      default_zone: The name of the default zone. This value can be
        overwritten by the different API calls.

    Raises:
      ValueError: When an invalid base_url is provided.
    """
    self._thread_pool = None
    self.credentials = credentials
    if base_url is None and hasattr(self, 'BASE_URL'):
      base_url = self.BASE_URL
    if base_url is None:
      base_url = DEFAULT_BASE_URL

    GoogleComputeEngineBase._check_url(base_url)

    self.base_url = base_url.rstrip('/')
    logging.basicConfig(format=LOG_FORMAT, level=logging_level)
    self.logger = logging.getLogger('GoogleComputeEngine')

    self._default_image = default_image
    self._default_machine_type = default_machine_type
    self._default_network = default_network
    self._default_network_interface = (default_network_interface or
                                       shortcuts.network(default_network))
    self._default_project = default_project
    self._default_zone = default_zone

  def __del__(self):
    self.wait_until_done()

  @property
  def default_image(self):
    return self._default_image

  @property
  def default_machine_type(self):
    return self._default_machine_type

  @property
  def default_network(self):
    return self._default_network

  @property
  def default_network_interface(self):
    return self._default_network_interface

  @property
  def default_project(self):
    return self._default_project

  @property
  def default_zone(self):
    return self._default_zone

  @default_image.setter
  def default_image(self, value):
    self._default_image = value

  @default_machine_type.setter
  def default_machine_type(self, value):
    self._default_machine_type = value

  @default_network.setter
  def default_network(self, value):
    self._default_network = value

  @default_network_interface.setter
  def default_network_interface(self, value):
    self._default_network_interface = value

  @default_project.setter
  def default_project(self, value):
    self._default_project = value

  @default_zone.setter
  def default_zone(self, value):
    self._default_zone = value

  @default_image.deleter
  def default_image(self):
    self._default_image = None

  @default_machine_type.deleter
  def default_machine_type(self):
    self._default_machine_type = None

  @default_network.deleter
  def default_network(self):
    self._default_network = 'default'

  @default_network_interface.deleter
  def default_network_interface(self):
    self._default_network_interface = shortcuts.network()

  @default_project.deleter
  def default_project(self):
    self._default_project = None

  @default_zone.deleter
  def default_zone(self):
    self._default_zone = None

  def wait_until_done(self):
    """Blocks until all outstanding operations are done.

    Any program that uses this library should call this method before
    exiting.
    """
    if self._thread_pool is not None:
      tp = self._thread_pool
      self._thread_pool = None
      tp.join()

  def _normalize(self, project, kind, resource):
    """Normalizes the URI for the given resource.

    A normalized resource URI contains the base URI, project
    identifier, and the resource identifier.

    Args:
      project: The name of the project.
      kind: The type of the resource (e.g., disks, images).
      resource: The name of the resource or the resource's URI.

    Returns:
      The URI to the given resource.
    """
    if resource.startswith(self.base_url):
      return resource

    if resource.startswith('projects/'):
      return '/'.join((self.base_url, resource[9:]))

    if resource.startswith('/projects/'):
      return '/'.join((self.base_url, resource[10:]))

    if resource.startswith(kind + '/'):
      return '/'.join((self.base_url, project, resource))

    return '/'.join((self.base_url, project, kind, resource))

  def _send_request(self, path, method='GET', request_body=None):
    while True:
      headers = {'authorization': 'OAuth ' + self.credentials.access_token}
      if request_body:
        headers['content-type'] = 'application/json'

      self.logger.info('Sending {0} request to {1}.'.format(method, path))
      if request_body:
        self.logger.debug('Request body: {0}'.format(request_body))

      response, data = httplib2.Http().request(
          path, method, request_body, headers)

      self.logger.debug('Received response: {0}'.format(response))
      if data:
        self.logger.debug('Response body: {0}'.format(data))

      if (response.status == 200 or
          response.status == 403 or
          response.status == 503):
        return json.loads(data)
      elif 200 <= response.status <= 299:
        break

      elif response.status == 401:
        self.credentials.refresh(httplib2.Http())
      elif response.status == 404:
        raise ValueError('Could not find resource: {0}'.format(path))
      else:
        raise ValueError('Received response code: {0}'.format(response.status))

  def _execute(self, request, blocking):
    """Calls the Google Compute Engine backend with the given parameters.

    Args:
      request: An instance of API_REQUEST named tuple describing the request.
      blocking: Wait for an asynchronous opration to complete before returning.

    Raises:
      ValueError: If there is a problem making the request or the given
        uri is mal-formed.

    Returns:
      A dict containing the response.
    """
    base = urlparse.urlsplit(self.base_url)

    query_params_list = []
    if request.query:
      for key, value in request.query.iteritems():
        value = urllib.quote_plus(str(value))
        query_params_list.append('{0}={1}'.format(key, value))

    path = urlparse.urlunsplit(
        (base.scheme, base.netloc,
         '{0}/{1}'.format(base.path.rstrip('/'), request.url),
         '&'.join(query_params_list), ''))

    GoogleComputeEngineBase._check_url(path)
    result = self._send_request(path, request.method, request.body)
    if blocking:
      result = self._wait_for(operation=result)
    return result

  def _wait_for(self, operation, timeout_secs=TIMEOUT_SECS):
    """Blocks until the given operation's status is DONE.

    Args:
      operation: The operation to poll. This should be a dict
        corresponding to an Operation resource.
      timeout_secs: The maximum amount of time this method will
        wait for completion of an operation.

    Raises:
      ValueError: If the timeout expires or the given resource is
        not an Operation.

    Returns:
      For non-delete operations, a tuple where the first element is a
      dict corresponding to the Operation and the second element is
      the object that was mutated. Deletes return just the operation.
    """
    if operation.get('kind') != 'compute#operation':
      raise ValueError('Only objects of type Operation can be polled.')

    self_link = operation.get('selfLink')
    if not self_link:
      raise ValueError('Invalid selfLink.')

    start_time_secs = time.time()
    delay = 0.0
    while True:
      self.logger.debug('Polling operation {0}...'.format(operation.get('id')))
      operation = self._send_request(self_link)

      current_time_secs = time.time()
      if current_time_secs - start_time_secs > timeout_secs:
        raise ValueError('Polling timed out.')

      if operation.get('status') == 'DONE':
        break

      delay = min(max(delay * 1.5, 1.0), 5.0)
      self.logger.debug('Operation has not completed. Polling again in {0} '
                        'seconds.'.format(delay))
      time.sleep(delay)

    self.logger.info('Operation is done.')

    if operation.get('operationType') == 'delete':
      return operation

    mutated_object = None
    if 'error' not in operation:
      target_link = operation.get('targetLink')
      mutated_object = self._send_request(target_link)

    return (operation, mutated_object)

  def _generate(self, method, uri, query_params, result_type):
    """Generates all resources described by the given parameters.

    This method makes the list methods easier to use by taking care of
    paging under the covers (since each list method can return at most
    100 resources).

    Args:
      method: The method to use to fetch the resources.
      uri: The location of the resources.
      query_params: Query parameters that can be used to filter the
        results.
      result_type: The type of the resource.

    Yields:
      One resource at a time.
    """
    query_params = dict(query_params)
    request = GoogleComputeEngineBase.API_REQUEST(
        method, uri, query_params, None)
    while True:
      result = self._execute(request, False)
      items = result.get('items')
      next_page_token = result.get('nextPageToken')
      if not items:
        break
      for item in items:
        if result_type:
          item = result_type.from_json(item, self)
        yield item
      if not next_page_token:
        break
      query_params['pageToken'] = next_page_token

  def _get_parsers(self):
    """Returns a dict that maps resource types to parsing functions.

    The resource types should be strings that identify a resource
    (e.g., 'compute#instance') and the parsing functions should
    construct an object defined in the generated code from a resource
    dict.
    """
    raise NotImplementedError('_get_parsers() must be implemented by subclass.')

  def _parse(self, val):
    """Parses the given val (a dict) into a resource object.

    Args:
      val: A dict representing a resource. The dict must contain a
        'kind' key that specifies the type of the resource (e.g.,
        'compute#instance'). If val is a two-element tuple, both
        elements in the tuple are converted.

    Raises:
      ValueError: If val is a tuple, but does not contain exactly two
        elements.
      KeyError: If any of the dicts passed in do not contain the key
        'kind' or if no conversion function exists for the given kind.

    Returns:
      An object that corresponds to the type of val if val is not a
      tuple, a two-element tuple that contains two objects
      corresponding to the elements of the tuple if val is a tuple,
       None if val is None, or val if val is an exception.
    """
    if val is None:
      return None
    if isinstance(val, BaseException):
      return val
    if isinstance(val, tuple):
      if len(val) != 2:
        raise ValueError('Expected two-element tuple.')
      return (self._parse(val[0]), self._parse(val[1]))

    kind = val.get('kind')
    if not kind:
      raise KeyError('No kind attribute found in input.')

    func = self._get_parsers().get(kind)
    if func is None:
      raise KeyError('No conversion function found.')
    return func(val, self)

  @staticmethod
  def _parse_project(self_link):
    """Extracts project name from the absolute URL of selfLink property."""
    if self_link is not None:
      match = GoogleComputeEngineBase._SELF_LINK_REGEX.match(self_link)
      if match:
        return match.group(1)
    return None

  @staticmethod
  def _combine(list1, list2):
    """Combines two sequences much like izip, allowing either to be None."""

    def all_nones():
      while True:
        yield None

    if list1 is not None:
      if list2 is not None:
        # This won't work for inputs being generators. Consider allowing them.
        if len(list1) != len(list2):
          raise ValueError('List of objects and names must be equal length')
        return itertools.izip(list1, list2)
      else:
        return itertools.izip(list1, all_nones())
    elif list2 is not None:
      return itertools.izip(all_nones(), list2)
    else:
      return []

  def _execute_list(self, requests, blocking):
    """Executes list of Api requests.

    Args:
      requests: Iterable of request, each is an instance of API_REQUEST named
      tuple defined above.
      blocking: Wait for asynchronous operations to complete before returning.

    Returns:
      List of response objects (unparsed).
    """
    if self._thread_pool is None:
      self._thread_pool = thread_pool.ThreadPool(THREAD_COUNT, RATE_LIMIT)
      self._thread_pool.start()

    tp = self._thread_pool
    futures = [tp.submit(self._execute, request, blocking)
               for request in requests]
    return [future.wait() for future in futures]

  def _parse_list(self, response_list):
    """Parse the results of the list execution.

    Args:
      response_list: List of responses from the Api.
    Returns:
      List of parsed objects.
    """
    return [self._parse(response) for response in response_list]

  @staticmethod
  def _check_url(url):
    """Ensures that the given URL conforms to the expected API URL.

    Args:
      url: The URL to check.

    Raises:
      ValueError: If the base URL is malformed.
    """
    parts = urlparse.urlsplit(url)
    expected_parts = urlparse.urlsplit(BASE_URL_TEMPLATE)
    version_regex = u'[a-z0-9]+'
    if (parts.scheme != expected_parts.scheme or
        parts.netloc != expected_parts.netloc or
        not re.search(expected_parts.path.format(version_regex), parts.path)):
      raise ValueError('Invalid base URL. Required format: ' +
                       BASE_URL_TEMPLATE.format('<version>'))

  @staticmethod
  def _strings_to_json(value):
    """Serializes iterable of strings to list. Promotes string to list.

    Args:
      value: the value to convert to list of strings. It can be a iterable of
      strings or an individual string, in which case it is promoted to list.
    Returns:
      List of strings.
    Raises:
      ValueError: If the value is None.
    """
    if value is None:
      raise ValueError('strings cannot be None.')
    elif isinstance(value, basestring):
      return [value]
    else:
      return list(value)

  @staticmethod
  def _json_to_strings(value):
    """Deserializes list of strings from json.

    Used by the generated code to parse the list of string values. Basically
    only creates copy of the list but tolerates None.

    Input: ['value1', 'value2', ... 'valueN'], or None

    Args:
      value: The list deserialized from json.
    Returns:
      List of strings extracted from the json list.
    """
    return None if value is None else list(value)


class ListObjectBase(object):
  """Common base class for all classes representing lists of objects."""
  __slots__ = ['__items']

  def __init__(self, items):
    self.__items = items

  def __iter__(self):
    if self.__items is not None:
      for i in self.__items:
        yield i

  def __len__(self):
    return len(self.__items) if self.__items is not None else 0

  def __getitem__(self, index):
    return self.items.__getitem__(index)
