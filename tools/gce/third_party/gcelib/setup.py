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

"""Setup script for the Google Compute Engine Client Library."""

try:
  from setuptools import setup
  print 'Loaded setuptools'
except ImportError:
  from distutils.core import setup
  print 'Loaded distutils.core'

INSTALL_REQUIRES = [
    'oauth2client>=1.0c2',
    'httplib2>=0.7.4',
    'python-gflags>=2.0',
    ]

setup(
    name='google-compute-engine-library',
    version='0.1',
    description='The Google Compute Engine Client Library.',
    author='Google Inc.',
    author_email='gc-team@google.com',
    url='http://code.google.com/p/google-compute-engine-tools/',
    install_requires=INSTALL_REQUIRES,
    packages=['gcelib'],
    license='Apache 2.0',
    keywords='google compute engine client library',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: POSIX',
                 'Topic :: Internet :: WWW/HTTP'])
