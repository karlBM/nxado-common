#!/bin/bash

set -e
python -m pip install -- upgrade pip
apt-get update -y && apt-get autoremove -y && apt-get autoclean -y
apt-get install _y gcc

apt-get -y intall libc-dev
apt-get -y install build-essential


pip install -r /tmp/reauirements.txt
exec "$@"