@echo off
setlocal enabledelayedexpansion
set MIN_VERSION=3.10

python --version >nul 2>&1
if %ERRORLEVEL%==0 (
    for /f "tokens=2 delims= " %%a in ('python --version') do set PY_VER=%%a
    echo Found Python version !PY_VER!

    for /f "tokens=1,2 delims=." %%m in ("!PY_VER!") do (
        set PY_MAJOR=%%m
        set PY_MINOR=%%n
    )

    for /f "tokens=1,2 delims=." %%m in ("%MIN_VERSION%") do (
        set MIN_MAJOR=%%m
        set MIN_MINOR=%%n
    )

    if !PY_MAJOR! GTR !MIN_MAJOR! (
        echo Python meets version requirement. Skipping install.
        goto :RUN_APP
    )
    if !PY_MAJOR! EQU !MIN_MAJOR! if !PY_MINOR! GEQ !MIN_MINOR! (
        echo Python meets version requirement. Skipping install.
        goto :RUN_APP
    )

    echo Python version too old. Installing latest...
) else (
    echo Python not found. Installing latest...
)

winget install -e --id Python.Python.3 --silent

:RUN_APP
set "PATH=%PATH%;%LOCALAPPDATA%\Programs\Python\Python310\Scripts;%LOCALAPPDATA%\Programs\Python\Python310\"
python Projeck_Å_GUI.py

:end
echo Done!
pause