@echo off
echo Building CEV2 Backend...
cd /d %~dp0
if exist build_new rmdir /s /q build_new
mkdir build_new
cd build_new

echo Clearing environment variables that might interfere with CMake...
set CMAKE_PREFIX_PATH=
set CMAKE_INCLUDE_PATH=
set CMAKE_LIBRARY_PATH=

echo Configuring with CMake...
cmake .. -G "Visual Studio 17 2022"
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
echo Executable should be in: %~dp0build_new\bin\Release\CEV2.exe 