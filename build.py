import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path

def main():
    """Build the CovEngineV2 application using PyInstaller"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Build CovEngineV2 with PyInstaller")
    parser.add_argument("--onefile", action="store_true", help="Build as a single executable file")
    args = parser.parse_args()
    
    print("Building CovEngineV2 with PyInstaller...")
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("PyInstaller is not installed. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Run PyInstaller with the appropriate spec file
    print("Running PyInstaller...")
    if args.onefile:
        spec_file = "CovEngineV2_OneFile.spec"
        print("Building in one-file mode...")
    else:
        spec_file = "CovEngineV2.spec"
        print("Building in one-directory mode...")
    
    subprocess.run(["pyinstaller", spec_file, "--clean"], check=True)
    
    # For one-directory mode, we need to manually copy some files
    if not args.onefile:
        # Check if the backend executable exists
        backend_exe = Path("backend/build/Release/CEV2.exe")
        if not backend_exe.exists():
            print(f"Error: Backend executable not found at {backend_exe}")
            return
        
        # Copy the backend executable to the dist folder
        print("Copying backend executable to dist folder...")
        os.makedirs("dist/CovEngineV2/backend/build/Release", exist_ok=True)
        shutil.copy2(backend_exe, "dist/CovEngineV2/backend/build/Release/")
        
        # Copy the batch file for creating restore points
        batch_file = Path("create_restore_point.bat")
        if batch_file.exists():
            print("Copying restore point batch file...")
            shutil.copy2(batch_file, "dist/CovEngineV2/")
        
        print("Build completed successfully!")
        print("The executable is located at: dist/CovEngineV2/CovEngineV2.exe")
    else:
        print("Build completed successfully!")
        print("The executable is located at: dist/CovEngineV2_OneFile.exe")

if __name__ == "__main__":
    main() 