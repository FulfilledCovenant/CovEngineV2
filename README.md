# CovEngineV2

A comprehensive system optimization and tweaking tool for Windows 10-11

## Features

- Performance optimization tweaks
- Gaming-specific optimizations
- Privacy enhancements
- Security hardening
- System monitoring

## Building from Source

### Prerequisites

- CMake 3.10 or higher
- C++ compiler with C++11 support
- Python 3.8 or higher
- Git

### Clone the Repository

```bash
git clone https://github.com/yourusername/CovEngineV2.git
cd CovEngineV2
```

### Build with CMake

```bash
# Create a build directory
mkdir build
cd build

# Configure the project
cmake ..

# Build the backend
cmake --build . --config Release

# Build the complete application (backend + frontend)
cmake --build . --target build_all --config Release
```

### Alternative Build Methods

You can also build the application using the provided scripts:

```bash
# Using the build script (Windows)
./build.bat

# Or using Python directly
python build.py
```

## Installation

After building, the application can be found in the `dist/CovEngineV2` directory.

## Usage

Run the application with administrator privileges:

```
dist/CovEngineV2/CovEngineV2.exe
```
