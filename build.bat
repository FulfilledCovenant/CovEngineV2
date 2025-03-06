@echo off
echo CovEngineV2 Build Script
echo -----------------------
echo 1. Build as one directory (recommended)
echo 2. Build as one file (single executable)
echo.

set /p choice=Enter your choice (1 or 2): 

if "%choice%"=="1" (
    echo Building CovEngineV2 as one directory...
    python build.py
) else if "%choice%"=="2" (
    echo Building CovEngineV2 as one file...
    python build.py --onefile
) else (
    echo Invalid choice. Please enter 1 or 2.
    goto :eof
)

if %errorlevel% equ 0 (
    echo Build completed successfully!
    if "%choice%"=="1" (
        echo The executable is located at: dist\CovEngineV2\CovEngineV2.exe
    ) else (
        echo The executable is located at: dist\CovEngineV2_OneFile.exe
    )
) else (
    echo Build failed with error code %errorlevel%
)
pause 