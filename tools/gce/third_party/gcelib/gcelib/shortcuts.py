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

"""A set of convenience functions for using Google Compute Engine."""


def network(network_name=None, external_ip=None):
  network_name = network_name or 'default'
  access_config = {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
  if external_ip:
    access_config['natIP'] = external_ip
  return [{'accessConfigs': [access_config],
           'network': network_name}]


def rw_disks(disk_names):
  disks = []
  for disk_name in disk_names:
    disks.append({'mode': 'READ_WRITE',
                  'type': 'PERSISTENT',
                  'source': disk_name})
  return disks


def ro_disks(disk_names):
  disks = []
  for disk_name in disk_names:
    disks.append({'mode': 'READ_ONLY',
                  'type': 'PERSISTENT',
                  'source': disk_name})
  return disks


def service_accounts(scopes=None, email='default'):
  scopes = scopes or []
  return [{'scopes': scopes,
           'email': email}]


def metadata(dictionary):
  items = [{'key': key, 'value': value}
           for key, value in dictionary.iteritems()]
  return {'items': items}
