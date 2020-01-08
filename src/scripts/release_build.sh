#!/usr/bin/env bash
set -ex

USERNAME=ppiitt123
IMAGE=fbng_backend

version=`cat ../VERSION`
echo "version: $version"
#rm -rf ../settings_local.py

docker build --no-cache -t ${USERNAME}/${IMAGE} -f ./Dockerfile ../
docker tag ${USERNAME}/${IMAGE}:latest ${USERNAME}/${IMAGE}:${version}
docker push ${USERNAME}/${IMAGE}:latest
docker push ${USERNAME}/${IMAGE}:${version}
