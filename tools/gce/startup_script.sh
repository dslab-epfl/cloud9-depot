#!/bin/bash -e
#
# Copyright 2012 EPFL. All rights reserved.
# Author: Stefan Bucur (stefan.bucur@epfl.ch)

METADATA_SERVER='http://metadata/0.1/meta-data'

CLOUD9_BINARY="gs://cloud9-binaries/cloud9.tar.gz"

gsutil cp ${CLOUD9_BINARY} /tmp
