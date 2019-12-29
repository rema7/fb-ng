#!/bin/bash

NODE_MODULES="./node_modules"

if [[ "$(ls -A $NODE_MODULES)" ]]; then
    echo "Node environment is ready. Clear it for reloading"
else
    echo "Node environment isn't ready."
    npm install --no-progress --ignore-optional
    npm rebuild fibers --force
fi

npm run dev:server
