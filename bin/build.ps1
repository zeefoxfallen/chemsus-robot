Push-Location -Path $PSScriptRoot

python -m venv --prompt "chemsus-robot .venv" ..\.venv

..\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

pip install -r ..\requirements.txt

pip list

deactivate

Pop-Location
