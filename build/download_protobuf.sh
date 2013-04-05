#!/usr/bin/env bash

# This script will download glog into third_party/glog and build it.

# Do NOT CHANGE this, unless you know what you're doing
PROTOBUF_SNAPSHOT="protobuf-2.4.1.tar.gz"

THIS_DIR="$(dirname "${0}")"
PROTOBUF_DIR="${THIS_DIR}/../third_party/protobuf"
PROTOBUF_DWD_DIR="${THIS_DIR}/../third_party/.downloads"
PROTOBUF_BUILD_DIR="${PROTOBUF_DIR}/../protobuf-install"
STAMP_FILE="${PROTOBUF_BUILD_DIR}/cr_build_revision"

PROTOBUF_URL="https://protobuf.googlecode.com/files/"

set -e

force_local_build=
while [[ $# > 0 ]]; do
  case $1 in
    --force-local-build)
      force_local_build=yes
      ;;
    --help)
      echo "usage: $0 [--force-local-build] "
      echo "--force-local-build: Force compilation"
      exit 1
      ;;
  esac
  shift
done

# Check if there's anything to be done, exit early if not.
if [[ -f "${STAMP_FILE}" ]]; then
  PREVIOUSLY_BUILT_REVISON=$(cat "${STAMP_FILE}")
  if [[ -z "$force_local_build" ]] && \
			 [[ "${PREVIOUSLY_BUILT_REVISON}" = "${PROTOBUF_SNAPSHOT}" ]]; then
    echo "Protobuf snapshot ${PROTOBUF_SNAPSHOT} already built."
    exit 0
  fi
fi
# To always force a new build if someone interrupts their build half way.
rm -f "${STAMP_FILE}"

PROTOBUF_OUTPUT="${PROTOBUF_DWD_DIR}/${PROTOBUF_SNAPSHOT}"

if [ ! -f "${PROTOBUF_OUTPUT}" ]; then
		mkdir -p "${PROTOBUF_DWD_DIR}"
		echo Downloading Protobuf snapshot "${PROTOBUF_SNAPSHOT}" at "${PROTOBUF_URL}"
		if which curl > /dev/null; then
				curl -L --fail "${PROTOBUF_URL}/${PROTOBUF_SNAPSHOT}" -o "${PROTOBUF_OUTPUT}"
		elif which wget > /dev/null; then
				wget "${PROTOBUF_URL}/${PROTOBUF_SNAPSHOT}" -O "${PROTOBUF_OUTPUT}"
		else
				echo "Neither curl nor wget found. Please install one of these."
				exit 1
		fi

		if [ ! -f "${PROTOBUF_OUTPUT}" ]; then
				echo Could not download Protobuf
				exit 1
		fi
		echo Protobuf downloaded successfully
else
		echo Protobuf snapshot already cached
fi

rm -rf "${PROTOBUF_DIR}"
rm -rf "${PROTOBUF_BUILD_DIR}"

mkdir -p "${PROTOBUF_DIR}"
mkdir -p "${PROTOBUF_BUILD_DIR}"
PROTOBUF_BUILD_DIR=$(readlink -f "${PROTOBUF_BUILD_DIR}")

tar -xzvf "${PROTOBUF_OUTPUT}" -C "${PROTOBUF_DIR}" --strip-components=1

# Echo all commands
set -x

NUM_JOBS=3
cd "${PROTOBUF_DIR}"
if [[ ! -f ./config.status ]]; then
	./configure --prefix="${PROTOBUF_BUILD_DIR}"
fi

make all -j"${NUM_JOBS}"
make install
cd -

echo "${PROTOBUF_SNAPSHOT}" >"${STAMP_FILE}"
