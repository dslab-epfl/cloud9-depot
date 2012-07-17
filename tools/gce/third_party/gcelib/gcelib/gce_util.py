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

"""An simple utilites for use with Google Compute Engine library."""

import collections
import ConfigParser
import datetime
import json
import os
import urllib

import gflags
import oauth2client.client
import oauth2client.file
import oauth2client.tools

gflags.FLAGS.auth_local_webserver = False

# Credential and configuration files.
GCE_CREDENTIALS_FILE = '~/.gce.credentials'
GCE_CONFIG_FILE = '~/.gce.config'

# Config file section name.
GCE_CONFIG_SECTION = 'gce_config'


GceDefaults = collections.namedtuple(
    'GceDefaults', ('project', 'image', 'machine_type', 'network', 'zone'))


def get_credentials():
  """Returns OAuth2 credentials for use with Google Compute Engine Api.

  Loads the credentials from the credentials file. If the credentials are
  missing or invalid, performs the OAuth2 authentication flow.

  Returns:
    oauth2client credentials object to use with the GoogleComputeEngine Api.
  """
  storage = oauth2client.file.Storage(os.path.expanduser(GCE_CREDENTIALS_FILE))
  credentials = storage.get()


  if credentials is None or credentials.invalid:
    flow = oauth2client.client.OAuth2WebServerFlow(
        client_id='1025389682001.apps.googleusercontent.com',
        client_secret='xslsVXhA7C8aOfSfb6edB6p6',
        scope='https://www.googleapis.com/auth/compute',
        user_agent='google-compute-engine-demo/0.1')
    credentials = oauth2client.tools.run(flow, storage)
  return credentials


class ServiceAccountCredentials(oauth2client.client.OAuth2Credentials):
  """Credentials object that uses service account scopes inside an instance."""

  def __init__(self, scopes='https://www.googleapis.com/auth/compute'):
    self.scopes = scopes
    access_token, token_expiry = self._internal_refresh()
    oauth2client.client.OAuth2Credentials.__init__(self, access_token, None,
                                                   None, None, token_expiry,
                                                   None, None)

  def _refresh(self, _):
    self.access_token, self.token_expiry = self._internal_refresh()

  def _internal_refresh(self):
    url = ('http://metadata/0.1/meta-data/service-accounts/default/'
           'acquire?scopes=' + self.scopes)
    data = json.loads(urllib.urlopen(url).read())
    return (data['accessToken'],
            datetime.datetime.utcfromtimestamp(data['expiresAt']))


def get_defaults():
  """Loads the default values to use with the GoogleComputeEngine Api.

  The default values are loaded from the configuration file.

  Returns:
    The GceDefaults named tuple with the default values.
  """

  def get_option(cfg, option, default=None):
    if cfg.has_option(GCE_CONFIG_SECTION, option):
      return cfg.get(GCE_CONFIG_SECTION, option)
    return default

  config = ConfigParser.RawConfigParser()
  config.read(os.path.expanduser(GCE_CONFIG_FILE))
  return GceDefaults(
      get_option(config, 'project'),
      get_option(config, 'image'),
      get_option(config, 'machine_type'),
      get_option(config, 'network', 'default'),
      get_option(config, 'zone'))
