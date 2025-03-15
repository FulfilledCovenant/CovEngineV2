@echo off
echo Building spoofer backend...

if not exist "build" mkdir build
cd build

cmake -G "Visual Studio 17 2022" -A Win32 ..
cmake --build . --config Release

if %ERRORLEVEL% NEQ 0 (
    echo Build failed!
    exit /b %ERRORLEVEL%
)

echo Build complete!

if not exist "..\bin" mkdir ..\bin
copy bin\Release\SPF.exe ..\bin\SPF.exe

echo Executable copied to bin directory
cd .. 