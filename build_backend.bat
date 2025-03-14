@echo off
echo Building CEV2 Backend...
cd /d %~dp0
if exist build rmdir /s /q build
mkdir build
cd build
cmake .. -G "Visual Studio 17 2022"
if %ERRORLEVEL% NEQ 0 (
    echo CMake configuration failed
    exit /b %ERRORLEVEL%
)
cmake --build . --config Release
if %ERRORLEVEL% NEQ 0 (
    echo Build failed
    exit /b %ERRORLEVEL%
)
echo Build completed successfully 