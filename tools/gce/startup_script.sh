#!/bin/bash -e
#
# Copyright 2012 EPFL. All rights reserved.
# Author: Stefan Bucur (stefan.bucur@epfl.ch)

METADATA_SERVER='http://metadata/0.1/meta-data'
SERVICE_ACCOUNT='default'
SCOPE='https://www.googleapis.com/auth/devstorage.read_write'
GOOGLE_STORAGE_PROJECT_ID=$(curl ${METADATA_SERVER}/attributes/gcs-id)

CLOUD9_BINARY="cloud9-binaries/cloud9.tar.gz"

ACCESS_TOKEN=$(wget -q -O - ${METADATA_SERVER}/service-accounts/${SERVICE_ACCOUNT}/acquire?${SCOPE} |
    python -c 'import json, sys; print json.load(sys.stdin)["accessToken"];')

rm -rf /tmp/cloud9.tar.gz

wget "https://commondatastorage.googleapis.com/${CLOUD9_BINARY}" \
    --header "Authorization: OAuth ${ACCESS_TOKEN}" \
    --header "x-goog-api-version: 2" \
    --header "x-goog-project-id: ${GOOGLE_STORAGE_PROJECT_ID}" \
		-O /tmp/cloud9.tar.gz
