#!/usr/bin/env bash

pushd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null

source ../.venv/bin/activate 

python3 ../bot/main.py 

deactivate 

popd > /dev/null