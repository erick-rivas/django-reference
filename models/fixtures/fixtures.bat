@ECHO OFF
setlocal enabledelayedexpansion
for %%f in (.\models\fixtures\*.yaml) do (
  if not %%f == .template.yaml (
    python manage.py loaddata .\models\fixtures\%%f
  )
)