@ECHO OFF

pushd %~dp0

call ..\.venv\Scripts\activate.bat

python ..\bot\main.py

call ..\.venv\Scripts\deactivate.bat

popd
