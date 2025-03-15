@echo off
echo Building CEV2 Backend...

set SRC_DIR=C:\Users\filefilza\Desktop\prioj\backend
set BUILD_DIR=C:\Users\filefilza\Desktop\prioj\backend\out_build
echo Using source directory: %SRC_DIR%
echo Using build directory: %BUILD_DIR%

if exist "%BUILD_DIR%" rmdir /s /q "%BUILD_DIR%"
mkdir "%BUILD_DIR%"
cd /d "%BUILD_DIR%"

echo Running CMake...
cmake -S "%SRC_DIR%" -B "%BUILD_DIR%" -G "Visual Studio 17 2022"
if %ERRORLEVEL% NEQ 0 (
    echo CMake configuration failed
    exit /b %ERRORLEVEL%
)

echo Building...
cmake --build "%BUILD_DIR%" --config Release
if %ERRORLEVEL% NEQ 0 (
    echo Build failed
    exit /b %ERRORLEVEL%
)

echo Build completed successfully
echo Executable should be in: %BUILD_DIR%\bin\Release\CEV2.exe

pause 