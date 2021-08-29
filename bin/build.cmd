@ECHO OFF

pushd %~dp0

if exist ..\.venv (

rmdir /S /Q ..\.venv

)

python -m venv --prompt "chemsus-robot .venv" ..\.venv

call ..\.venv\Scripts\activate.bat

python -m pip install --upgrade pip

pip install -r ..\requirements.txt

pip list

call ..\.venv\Scripts\deactivate.bat

popd
