# CovEngineV2 Build Instructions

This document provides instructions on how to build CovEngineV2 into a executable.

## Prerequisites

- Python 3.8 or higher
- CMake 3.10 or higher (for building the backend)
- Visual Studio 2022 or higher with C++ development tools
- PyInstaller (will be installed automatically if not present)
- Windows operating system (the application is designed for Windows)

## Building the Application

### Building the Backend

The backend can be built using either the provided batch script or manual commands.

#### Using the Build Script (Recommended)

1. Navigate to the `backend` directory
2. Run the `build_final.bat` script
3. Wait for the build process to complete

The backend executable will be created at `backend/out_build/bin/Release/CEV2.exe`.

#### Manual Build

If you prefer to build manually, follow these steps:

1. Navigate to the `backend` directory
2. Create a build directory: `mkdir out_build && cd out_build`
3. Generate build files with CMake: `cmake -S .. -B . -G "Visual Studio 17 2022"`
4. Build the project: `cmake --build . --config Release`

Note: If you encounter "Error: could not load cache" issues, use the `-S` and `-B` flags as shown above to explicitly specify source and build directories.

### Building the Frontend

#### Using the Build Script

1. Make sure you have Python installed and added to your PATH.
2. Run the `build.bat` file by double-clicking it.
3. Choose the build mode:
   - Option 1: Build as one directory (recommended) - Creates a folder with the executable and supporting files
   - Option 2: Build as one file - Creates a single executable file (Note: This may take longer to build and start up)

#### Manual Build

If you prefer to build manually, you can use the following commands:

##### One Directory Mode (Recommended)
```
python build.py
```

##### One File Mode
```
python build.py --onefile
```

## Build Output

### One Directory Mode
The build output will be located in the `dist/CovEngineV2` directory. The main executable is `CovEngineV2.exe`.

### One File Mode
The build output will be a single executable file located at `dist/CovEngineV2.exe`.

## Distribution

To distribute the application:

### One Directory Mode
1. Copy the entire `dist/CovEngineV2` directory to the target machine.
2. Run `CovEngineV2.exe` to start the application.

### One File Mode
1. Copy the `dist/CovEngineV2.exe` file to the target machine.
2. Run the executable to start the application.

## Notes

- Requires administrator privileges to apply certain tweaks.
- Some tweaks may require a system restart to take effect.
- A system restore point is created before applying tweaks for safety.

## Troubleshooting

If you encounter any issues during the build process:

1. Make sure you have the latest version of Python and CMake installed.
2. Try running the build script with administrator privileges.
3. Check that the backend executable (`CEV2.exe`) is present in the correct directory.
4. If PyInstaller fails, try installing it manually with `pip install pyinstaller`.
5. If CMake fails with "Error: could not load cache", try using the batch file or the manual build with explicit directory paths.

If the application fails to run after building:

1. Make sure all required files are present in the distribution directory.
2. Check that the backend executable is properly located.
3. Run the application with administrator privileges.
4. Check the Windows Event Viewer for any error messages. 