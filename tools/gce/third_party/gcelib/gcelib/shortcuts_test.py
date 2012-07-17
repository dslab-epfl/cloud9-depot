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

"""Tests for the shortcut functions."""

import unittest

import shortcuts


class ShortcutsTests(unittest.TestCase):

  def test_network(self):
    self.assertEqual(
        shortcuts.network(),
        [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}],
          'network': 'default'}])

    self.assertEqual(
        shortcuts.network(None),
        [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}],
          'network': 'default'}])

    self.assertEqual(
        shortcuts.network('default'),
        [{'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}],
          'network': 'default'}])

    self.assertEqual(
        shortcuts.network('default', external_ip='123.123.123.123'),
        [{'accessConfigs': [
            {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT',
             'natIP': '123.123.123.123'}],
          'network': 'default'}])

  def test_rw_disks(self):
    self.assertEqual(
        shortcuts.rw_disks([]),
        [])

    self.assertEqual(
        shortcuts.rw_disks(['disk1']),
        [{'source': 'disk1',
          'type': 'PERSISTENT',
          'mode': 'READ_WRITE'}])

    self.assertEqual(
        shortcuts.rw_disks(['disk1', 'disk2']),
        [{'source': 'disk1',
          'type': 'PERSISTENT',
          'mode': 'READ_WRITE'},
         {'source': 'disk2',
          'type': 'PERSISTENT',
          'mode': 'READ_WRITE'}])

  def test_ro_disks(self):
    self.assertEqual(
        shortcuts.ro_disks([]),
        [])

    self.assertEqual(
        shortcuts.ro_disks(['disk1']),
        [{'source': 'disk1',
          'type': 'PERSISTENT',
          'mode': 'READ_ONLY'}])

    self.assertEqual(
        shortcuts.ro_disks(['disk1', 'disk2']),
        [{'source': 'disk1',
          'type': 'PERSISTENT',
          'mode': 'READ_ONLY'},
         {'source': 'disk2',
          'type': 'PERSISTENT',
          'mode': 'READ_ONLY'}])

  def test_service_accounts(self):
    self.assertEqual(
        shortcuts.service_accounts(),
        [{'scopes': [],
          'email': 'default'}])

    self.assertEqual(
        shortcuts.service_accounts(['a', 'b']),
        [{'scopes': ['a', 'b'],
          'email': 'default'}])

    self.assertEqual(
        shortcuts.service_accounts(['a', 'b'],
                                   email='42@developer.gserviceaccount.com'),
        [{'scopes': ['a', 'b'],
          'email': '42@developer.gserviceaccount.com'}])

  def test_metadata(self):
    self.assertEqual(
        shortcuts.metadata({}),
        {'items': []})

    self.assertEqual(
        shortcuts.metadata({'key': 'val'}),
        {'items': [{'key': 'key', 'value': 'val'}]})

    # dictionaries don't have well-defined ordering
    generated = shortcuts.metadata({'key1': 'val1', 'key2': 'val2'})['items']
    expected = [{'key': 'key1', 'value': 'val1'},
                {'key': 'key2', 'value': 'val2'}]
    self.assertEqual(
        sorted(generated, key=lambda i: i['key']),
        sorted(expected, key=lambda i: i['key']))


if __name__ == '__main__':
  unittest.main()
