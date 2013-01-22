#!/usr/bin/env bash

# This script will download glog into third_party/glog and build it.

# Do NOT CHANGE this, unless you know what you're doing
GLOG_SNAPSHOT="glog-0.3.1-1.tar.gz"


THIS_DIR="$(dirname "${0}")"
GLOG_DIR="${THIS_DIR}/../third_party/glog"
GLOG_DWD_DIR="${THIS_DIR}/../third_party/.downloads"
GLOG_BUILD_DIR="${GLOG_DIR}/../glog-install"
STAMP_FILE="${GLOG_BUILD_DIR}/cr_build_revision"

GLOG_URL="http://google-glog.googlecode.com/files/"

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
			 [[ "${PREVIOUSLY_BUILT_REVISON}" = "${GLOG_SNAPSHOT}" ]]; then
    echo "Glog snapshot ${GLOG_SNAPSHOT} already built."
    exit 0
  fi
fi
# To always force a new build if someone interrupts their build half way.
rm -f "${STAMP_FILE}"

GLOG_OUTPUT="${GLOG_DWD_DIR}/${GLOG_SNAPSHOT}"

if [ ! -f "${GLOG_OUTPUT}" ]; then
		mkdir -p "${GLOG_DWD_DIR}"
		echo Downloading Glog snapshot "${GLOG_SNAPSHOT}" at "${GLOG_URL}"
		if which curl > /dev/null; then
				curl -L --fail "${GLOG_URL}/${GLOG_SNAPSHOT}" -o "${GLOG_OUTPUT}"
		elif which wget > /dev/null; then
				wget "${GLOG_URL}/${GLOG_SNAPSHOT}" -O "${GLOG_OUTPUT}"
		else
				echo "Neither curl nor wget found. Please install one of these."
				exit 1
		fi

		if [ ! -f "${GLOG_OUTPUT}" ]; then
				echo Could not download Glog
				exit 1
		fi
		echo Glog downloaded successfully
else
		echo Glog snapshot already cached
fi

rm -rf "${GLOG_DIR}"
rm -rf "${GLOG_BUILD_DIR}"

mkdir -p "${GLOG_DIR}"
mkdir -p "${GLOG_BUILD_DIR}"
GLOG_BUILD_DIR=$(readlink -f "${GLOG_BUILD_DIR}")

tar -xzvf "${GLOG_OUTPUT}" -C "${GLOG_DIR}" --strip-components=1

# Echo all commands
set -x

NUM_JOBS=3
cd "${GLOG_DIR}"
if [[ ! -f ./config.status ]]; then
	./configure --prefix="${GLOG_BUILD_DIR}"
fi

make all -j"${NUM_JOBS}"
make install
cd -

echo "${GLOG_SNAPSHOT}" >"${STAMP_FILE}"
