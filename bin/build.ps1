Push-Location -Path $PSScriptRoot

$venvLocation = "..\.venv"

if (Test-Path $venvLocation)
{
  Remove-Item -Recurse $venvLocation
}

python -m venv --prompt "chemsus-robot .venv" $venvLocation

& "$venvLocation\Scripts\Activate.ps1"

python -m pip install --upgrade pip

pip install -r ..\requirements.txt

pip list

deactivate

Pop-Location
