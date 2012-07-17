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

"""Tests for gce_base."""

import unittest

import gce_base

class OperationMock(object):

  @staticmethod
  def load_from_dict(unused_val, unused_gce):
    return OperationMock()


class InstanceMock(object):

  @staticmethod
  def load_from_dict(unused_val, unused_gce):
    return InstanceMock()


class GoogleComputeEngineBaseTests(unittest.TestCase):
  """Tests for GoogleComputeEngineBase."""

  def setUp(self):
    self.gce = gce_base.GoogleComputeEngineBase(
        None,
        base_url='https://www.googleapis.com/compute/v1/projects/')

  def tearDown(self):
    pass#self.gce.shutdown()


  def test_normalize(self):
    """Tests resource normalization."""
    self.assertEqual(
        self.gce._normalize('my-project', 'instances', 'my-instance'),
        'https://www.googleapis.com/compute/v1/projects/my-project/instances/'
        'my-instance')

    self.assertEqual(
        self.gce._normalize('my-project', 'instances', 'instances/my-instance'),
        'https://www.googleapis.com/compute/v1/projects/my-project/instances/'
        'my-instance')

    self.assertEqual(
        self.gce._normalize('my-project', 'instances',
                            'projects/my-project/instances/my-instance'),
        'https://www.googleapis.com/compute/v1/projects/my-project/instances/'
        'my-instance')

    self.assertEqual(
        self.gce._normalize('my-project', 'instances', 'instances'),
        'https://www.googleapis.com/compute/v1/projects/my-project/instances/'
        'instances')

    self.assertEqual(
        self.gce._normalize('projectsprojects', 'instances',
                            'projects/projectsprojects/instances/my-instance'),
        'https://www.googleapis.com/compute/v1/projects/projectsprojects/'
        'instances/my-instance')

    self.assertEqual(
        self.gce._normalize('my-project', 'images', 'ubuntu-12-04-v20120503'),
        'https://www.googleapis.com/compute/v1/projects/my-project/images/'
        'ubuntu-12-04-v20120503')

    self.assertEqual(
        self.gce._normalize('my-project', 'images',
                            'projects/google/images/ubuntu-12-04-v20120503'),
        'https://www.googleapis.com/compute/v1/projects/google/images/'
        'ubuntu-12-04-v20120503')

  def test_defaults(self):
    """Tests the default properties."""
    self.assertEqual(self.gce.default_image, None)
    self.assertEqual(self.gce.default_machine_type, None)
    self.assertEqual(
        self.gce.default_network_interface,
        [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}],
          'network': 'default'}])
    self.assertEqual(self.gce.default_network, 'default')
    self.assertEqual(self.gce.default_project, None)
    self.assertEqual(self.gce.default_zone, None)

    self.gce.default_image = (
        'projects/google/images/ubuntu-12-04-v20120503')
    self.gce.default_machine_type = 'n1.standard-1-ssd'
    self.gce.default_network = 'my-network'
    self.gce.default_network_interface = (
        [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}],
          'network': 'my-network-interface'}])
    self.gce.default_project = 'my-project'
    self.gce.default_zone = 'us-east-a'

    self.assertEqual(self.gce.default_image,
                     'projects/google/images/ubuntu-12-04-v20120503')
    self.assertEqual(self.gce.default_machine_type, 'n1.standard-1-ssd')
    self.assertEqual(self.gce.default_network, 'my-network')
    self.assertEqual(
        self.gce.default_network_interface,
        [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}],
          'network': 'my-network-interface'}])
    self.assertEqual(self.gce.default_project, 'my-project')
    self.assertEqual(self.gce.default_zone, 'us-east-a')

    del self.gce.default_image
    del self.gce.default_machine_type
    del self.gce.default_network
    del self.gce.default_network_interface
    del self.gce.default_project
    del self.gce.default_zone

    self.assertEqual(self.gce.default_image, None)
    self.assertEqual(self.gce.default_machine_type, None)
    self.assertEqual(self.gce.default_network, 'default')
    self.assertEqual(
        self.gce.default_network_interface,
        [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}],
          'network': 'default'}])
    self.assertEqual(self.gce.default_project, None)
    self.assertEqual(self.gce.default_zone, None)

    gce = gce_base.GoogleComputeEngineBase(
        None,
        default_image='projects/google/images/ubuntu-12-04-v20120503',
        default_machine_type='n1.standard-1-ssd',
        default_network='my-network',
        default_network_interface=(
            [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT',
                                 'name': 'External NAT'}],
              'network': 'my-network-interface'}]),
        default_project='my-project',
        default_zone='us-east-a')

    self.assertEqual(gce.default_image,
                     'projects/google/images/ubuntu-12-04-v20120503')
    self.assertEqual(gce.default_machine_type, 'n1.standard-1-ssd')
    self.assertEqual(gce.default_network, 'my-network')
    self.assertEqual(
        gce.default_network_interface,
        [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}],
          'network': 'my-network-interface'}])
    self.assertEqual(gce.default_project, 'my-project')
    self.assertEqual(gce.default_zone, 'us-east-a')

    gce = gce_base.GoogleComputeEngineBase(
        None,
        default_network='my-network')
    self.assertEqual(
        gce.default_network_interface,
        [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}],
          'network': 'my-network'}])

  def test_execute_with_http(self):
    """Ensures that _execute() will not communicate over HTTP."""
    self.assertRaises(ValueError,
                      gce_base.GoogleComputeEngineBase,
                      credentials=None,
                      base_url='http://www.googleapis.com/compute/v1/projects/')

  def test_execute(self):
    """Tests _execute()'s ability to build up a correct request URL."""

    def mock_send_request(path, method, request_body):
      self.assertEqual(
          path,
          'https://www.googleapis.com/compute/v1/projects/my-project/'
          'instances?filter=name%2Beq%2B%27.%2A%2Fmy_instance_%5B0-9%5D%2B%27'
          '&pageToken='
          'CghJTlNUQU5DRRIhNzQyMzg3MDc3NTUuY3JlYXRlZC1qdW4tNi1udW0t'
          '&maxResults=100')
      self.assertEqual(method, 'GET')
      self.assertEqual(request_body, None)

    query_params = {
        'pageToken': 'CghJTlNUQU5DRRIhNzQyMzg3MDc3NTUuY3JlYXRlZC1qdW4tNi1udW0t',
        'filter': 'name+eq+\'.*/my_instance_[0-9]+\'',
        'maxResults': 100}

    self.gce._send_request = mock_send_request
    self.gce._execute(gce_base.GoogleComputeEngineBase.API_REQUEST(
        'GET', 'my-project/instances', query_params, None), False)

  def test_convert(self):
    """Ensures that _convert() correctly parses dict and tuples of dicts."""

    def get_parsers():
      """Returns a dict making kinds to parsers."""
      return {
          'compute#operation': OperationMock.load_from_dict,
          'compute#instance': InstanceMock.load_from_dict}

    def get_empty_parsers():
      """Returns a dict that contains no kind-to-parser mappings."""
      return {}

    self.gce._get_parsers = get_parsers

    self.assertEqual(self.gce._parse(None), None)
    self.assertEqual(self.gce._parse((None, None)),
                     (None, None))
    self.assertRaises(ValueError, self.gce._parse, (None, None, None))
    value_error = ValueError()
    self.assertEqual(self.gce._parse(value_error), value_error)

    operation = {
        'status': 'DONE',
        'kind': 'compute#operation',
        'name': '.../operation-1339021242481-4c1d52d7d64f0-63c9dc72',
        'startTime': '2012-06-06T22:20:42.601',
        'insertTime': '2012-06-06T22:20:42.481',
        'targetId': '12884714477555140369',
        'targetLink': 'https://googleapis.com/compute/.../instances/x-1000',
        'operationType': 'insert',
        'progress': 100,
        'endTime': '2012-06-06T22:20:49.268',
        'id': '12907884892091471776',
        'selfLink': 'https://googleapis.com/compute/...d64f0-63c9dc72',
        'user': 'bugsbunny@google.com'}

    instance = {
        'status': 'STAGING',
        'kind': 'compute#instance',
        'machineType': 'https://googleapis.com/compute/.../standard-1-cpu',
        'name': 'projects/my-project/instances/x-1000',
        'zone': 'https://googleapis.com/compute/.../zones/us-east-a',
        'tags': [],
        'image': 'https://googleapis.com/compute/.../images/ubuntu',
        'disks': [
            {
                'index': 0,
                'kind': 'compute#instanceDisk',
                'type': 'EPHEMERAL',
                'mode': 'READ_WRITE'
                }
            ],
        'networkInterfaces': [
            {
                'networkIP': '10.211.197.175',
                'kind': 'compute#instanceNetworkInterface',
                'accessConfigs': [
                    {
                        'type': 'ONE_TO_ONE_NAT',
                        'name': 'External NAT',
                        'natIP': '173.255.120.98'
                        }
                    ],
                'name': 'nic0',
                'network': 'https://googleapis.com/compute/.../networks/default'
                }
            ],
        'id': '12884714477555140369',
        'selfLink': 'https://googleapis.com/compute/.../instances/x-1000',
        'description': ''}

    self.assertRaises(ValueError, self.gce._parse, (operation, instance, None))

    res = self.gce._parse(operation)
    self.assertTrue(isinstance(res, OperationMock))
    res = self.gce._parse(instance)
    self.assertTrue(isinstance(res, InstanceMock))

    res = self.gce._parse((operation, None))
    self.assertTrue(isinstance(res[0], OperationMock))
    self.assertEqual(res[1], None)

    res = self.gce._parse((operation, instance))
    self.assertTrue(isinstance(res[0], OperationMock))
    self.assertTrue(isinstance(res[1], InstanceMock))

    del operation['kind']
    self.assertRaises(KeyError, self.gce._parse, operation)

    self.gce._get_parsers = get_empty_parsers
    self.assertRaises(KeyError, self.gce._parse, instance)

  def test_project_from_self_link(self):
    parse = gce_base.GoogleComputeEngineBase._parse_project

    self.assertEqual(
        parse('http://googleapis.com/compute/v1/projects/my-project'),
        'my-project')
    self.assertEqual(
        parse('https://googleapis.com/compute/v1beta11/projects/my-project/'),
        'my-project')
    self.assertEqual(
        parse('https://googleapis.com/compute/v1beta11/projects'
              '/my-project/instances/foo'),
        'my-project')
    self.assertEqual(
        parse('//googleapis.com/compute/v1beta11/projects/my-project/xxxx'),
        None)
    self.assertEqual(
        parse('http://googleapis.com/invalid/version/projects/my-project'),
        None)
    self.assertEqual(
        parse('http://googleapis.com/compute/version/noprojects/my-project'),
        None)
    self.assertEqual(
        parse('https://googleapis.com/compute/version/projects/'),
        None)

  def test_check_url(self):
    """Ensures that _check_url() raises an exception on bad API URLs."""
    check = gce_base.GoogleComputeEngineBase._check_url
    # Success cases.
    check('https://www.googleapis.com/compute/v1/projects/')
    check('https://www.googleapis.com/compute/v1beta12/projects/')

    # Failure cases.
    self.assertRaises(ValueError, check, '')
    self.assertRaises(ValueError, check,
                      'http://www.googleapis.com/compute/v1/projects/')
    self.assertRaises(ValueError, check,
                      'https://googleapis.com/compute/v1/projects/')
    self.assertRaises(ValueError, check,
                      'https://www.gmail.com/compute/v1/projects/')
    self.assertRaises(ValueError, check,
                      'http://www.googleapis.com/compute//projects/')
    self.assertRaises(ValueError, check,
                      'http://www.googleapis.com/compute/BAD_VERSION/projects/')
    self.assertRaises(ValueError, check,
                      'http://www.googleapis.com/compute/v1/')
    self.assertRaises(ValueError, check,
                      'http://www.googleapis.com/compute/v1/projects')
    self.assertRaises(ValueError, check,
                      'www.googleapis.com/compute/v1/projects')
    self.assertRaises(ValueError, check,
                      'https://www.googleapis.com/v1/projects')


if __name__ == '__main__':
  unittest.main()
