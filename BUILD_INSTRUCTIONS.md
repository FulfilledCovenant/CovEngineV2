# CovEngineV2 Build Instructions

This document provides instructions on how to build CovEngineV2 into a standalone executable.

## Prerequisites

- Python 3.8 or higher
- PyInstaller (will be installed automatically if not present)
- Windows operating system (the application is designed for Windows)

## Building the Application

### Using the Build Script

1. Make sure you have Python installed and added to your PATH.
2. Run the `build.bat` file by double-clicking it.
3. Choose the build mode:
   - Option 1: Build as one directory (recommended) - Creates a folder with the executable and supporting files
   - Option 2: Build as one file - Creates a single executable file

### Manual Build

If you prefer to build manually, you can use the following commands:

#### One Directory Mode (Recommended)
```
python build.py
```

#### One File Mode
```
python build.py --onefile
```

## Build Output

### One Directory Mode
The build output will be located in the `dist/CovEngineV2` directory. The main executable is `CovEngineV2.exe`.

### One File Mode
The build output will be a single executable file located at `dist/CovEngineV2_OneFile.exe`.

## Distribution

To distribute the application:

### One Directory Mode
1. Copy the entire `dist/CovEngineV2` directory to the target machine.
2. Run `CovEngineV2.exe` to start the application.

### One File Mode
1. Copy the `dist/CovEngineV2_OneFile.exe` file to the target machine.
2. Run the executable to start the application.

## Notes

- The application requires administrator privileges to apply certain tweaks.
- Some tweaks may require a system restart to take effect.
- A system restore point is created before applying tweaks for safety.

## Troubleshooting

If you encounter any issues during the build process:

1. Make sure you have the latest version of Python installed.
2. Try running the build script with administrator privileges.
3. Check that the backend executable (`CEV2.exe`) is present in the `backend/build/Release` directory.
4. If PyInstaller fails, try installing it manually with `pip install pyinstaller`.

If the application fails to run after building:

1. Make sure all required files are present in the distribution directory.
2. Check that the backend executable is properly located.
3. Run the application with administrator privileges.
4. Check the Windows Event Viewer for any error messages. 