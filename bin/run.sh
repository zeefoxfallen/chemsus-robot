#!/usr/bin/env bash

pushd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null

python3 -m venv --prompt "chemsus-robot .venv" ../.venv

bash -c "source ../.venv/bin/activate ;\
python3 ../bot/main.py ;\
deactivate "

popd > /dev/null