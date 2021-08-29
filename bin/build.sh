#!/usr/bin/env bash

pushd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null

python3 -m venv --prompt "chemsus-robot .venv" ../.venv

source ../.venv/bin/activate 

python3 -m pip install --upgrade pip 

pip install -r ../requirements.txt 

pip list 

deactivate 

popd > /dev/null