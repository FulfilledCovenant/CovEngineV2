import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path

def main():


    parser = argparse.ArgumentParser(description="Build CovEngineV2 with PyInstaller")
    parser.add_argument("--onefile", action="store_true", help="Build as a single executable file")
    args = parser.parse_args()
    
    print("Building CovEngineV2 with PyInstaller...")
    

    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("PyInstaller is not installed. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
   
    print("Running PyInstaller...")
    if args.onefile:
        spec_file = "CovEngineV2_OneFile.spec"
        print("Building in one-file mode...")
    else:
        spec_file = "CovEngineV2.spec"
        print("Building in one-directory mode...")
    
    subprocess.run(["pyinstaller", spec_file, "--clean"], check=True)
    
    
    if not args.onefile:
       
        backend_exe = Path("backend/out_build/bin/Release/CEV2.exe")
        if not backend_exe.exists():
            print(f"Error: Backend executable not found at {backend_exe}")
            print("Checking alternative backend locations...")
            
            alt_locations = [
                Path("backend/build/bin/Release/CEV2.exe"),
                Path("backend/build/Release/CEV2.exe"),
                Path("backend/build_new/bin/Release/CEV2.exe"),
                Path("backend/build_fix/bin/Release/CEV2.exe")
            ]
            
            for alt_path in alt_locations:
                if alt_path.exists():
                    print(f"Found backend at alternate location: {alt_path}")
                    backend_exe = alt_path
                    break
            else:
                print("Error: Could not find backend executable in any known location.")
                return
        
        target_dir = Path("dist/CovEngineV2/backend/bin/Release")
        os.makedirs(target_dir, exist_ok=True)
        
        print(f"Copying backend executable from {backend_exe} to {target_dir}...")
        shutil.copy2(backend_exe, target_dir)
        
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