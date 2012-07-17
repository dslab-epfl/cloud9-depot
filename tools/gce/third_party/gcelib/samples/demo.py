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

"""A simple program that demonstrates the new Google Compute Engine API.

Be sure to read the comments in main() before running this script. You
must set your project below. Your project should have quota for 10
instances and 10 CPUs.

Assuming this script runs to completion successfully, it will clean up
after itself.
"""

import logging

from gcelib import gce_util
from gcelib import gce_v1beta12
from gcelib import shortcuts

# Project-related configuration.
DEFAULT_PROJECT = None  # Your project name goes here.
DEFAULT_ZONE = 'us-east-a'
DEFAULT_IMAGE = 'projects/google/images/ubuntu-12-04-v20120621'
DEFAULT_MACHINE_TYPE = 'standard-1-cpu'

# Change logging to INFO to see more or to DEBUG to see even more!
LOG_LEVEL = logging.ERROR


def get_instances_by_zone(api):
  """Returns a dict mapping zones to number of instances."""
  result = {}
  for instance in api.all_instances():
    key = instance.zone
    result[key] = 1 + result.get(key, 0)
  return result


def main():
  # Performs the oauth2 dance.
  credentials = gce_util.get_credentials()

  # Grabs default values. Defaults can be saved in ~/.gce.config in
  # the following format:
  #
  # [gce_config]
  # project: my-project
  # image: projects/google/images/ubuntu-12-04-v20120621
  # zone: us-east-a
  # machine_type: standard-1-cpu
  defaults = gce_util.get_defaults()

  if DEFAULT_PROJECT is None and defaults.project is None:
    print 'Please specify a default project by editing DEFAULT_PROJECT in'
    print 'this script or by using a ~/gce.config file.'
    exit(1)

  # Constructs an instance of GoogleComputeEngine.
  api = gce_v1beta12.GoogleComputeEngine(
      credentials,
      logging_level=LOG_LEVEL,
      default_project=defaults.project or DEFAULT_PROJECT,
      default_zone=defaults.zone or DEFAULT_ZONE,
      default_image=defaults.image or DEFAULT_IMAGE,
      default_machine_type=defaults.machine_type or DEFAULT_MACHINE_TYPE)

  # Prints project info.
  print api.get_project()

  # Creates an instance asynchronously.
  print api.insert_instance(
      'i-was-created-asynchronously',
      networkInterfaces=shortcuts.network(),
      blocking=False)

  # Creates 9 test instances synchronously.
  names = ['test-instance-{0}'.format(i) for i in xrange(9)]
  print api.insert_instances(names, networkInterfaces=shortcuts.network())

  # Prints the names of all instances in the given project.
  for instance in api.all_instances():
    print instance.name

  # Prints the number of instances by zone.
  print get_instances_by_zone(api)

  # Deletes the asynchronously-created instance.
  print api.delete_instance('i-was-created-asynchronously', blocking=False)

  # Deletes the test instances synchronously.
  print api.delete_instances(names)

  # Prints the number of operations.
  print len(list(api.all_operations()))

  api.wait_until_done()


if __name__ == '__main__':
  main()
