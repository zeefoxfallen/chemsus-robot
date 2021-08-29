Push-Location -Path $PSScriptRoot

..\.venv\Scripts\Activate.ps1

..\bot\main.py

deactivate

Pop-Location