#!/usr/bin/env bash

pushd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null

venvLocation=../.venv

if [ -d "$venvLocation" ] ; then
    rm -rf "$venvLocation" 
fi

python3 -m venv --prompt "chemsus-robot .venv" "$venvLocation"

source "$venvLocation/bin/activate"

python3 -m pip install --upgrade pip 

pip install -r ../requirements.txt 

pip list 

deactivate 

popd > /dev/null