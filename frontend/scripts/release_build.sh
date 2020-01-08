#!/usr/bin/env bash
set -ex

USERNAME=ppiitt123
IMAGE=fbng_frontend

cd ../

version=$(cat ./package.json | grep version | head -1 | awk -F: '{ print $2 }' | sed 's/[\",]//g' | tr -d '[[:space:]]')
NODE_MODULES="./node_modules"

if [[ "$(ls -A $NODE_MODULES)" ]]; then
    echo "Node environment is ready. Clear it for reloading"
else
    echo "Node environment isn't ready."
    npm install --no-progress --ignore-optional
    npm rebuild fibers --force
fi

npm run build:prod

docker build --no-cache -t ${USERNAME}/${IMAGE} -f ./scripts/Dockerfile ./
docker tag ${USERNAME}/${IMAGE}:latest ${USERNAME}/${IMAGE}:${version}
docker push ${USERNAME}/${IMAGE}:latest
docker push ${USERNAME}/${IMAGE}:${version}
