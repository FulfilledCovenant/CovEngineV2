@echo off
echo Building CEV2 Backend...

set BACKEND_DIR=C:\Users\filefilza\Desktop\prioj\backend
set BUILD_DIR=%BACKEND_DIR%\build_fix
echo Working with:
echo - Backend dir: %BACKEND_DIR%
echo - Build dir: %BUILD_DIR%

if exist %BUILD_DIR% rmdir /s /q %BUILD_DIR%
mkdir %BUILD_DIR%
cd /d %BUILD_DIR%

echo Clearing environment variables that might interfere with CMake...
set CMAKE_PREFIX_PATH=
set CMAKE_INCLUDE_PATH=
set CMAKE_LIBRARY_PATH=

echo Configuring with CMake...
cmake %BACKEND_DIR% -G "Visual Studio 17 2022"
if %ERRORLEVEL% NEQ 0 (
    echo CMake configuration failed
    exit /b %ERRORLEVEL%
)

echo Building with CMake...
cmake --build . --config Release
if %ERRORLEVEL% NEQ 0 (
    echo Build failed
    exit /b %ERRORLEVEL%
)

echo Build completed successfully
echo Executable should be in: %BUILD_DIR%\bin\Release\CEV2.exe 