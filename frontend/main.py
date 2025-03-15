import sys
import os
import subprocess
import logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QMessageBox
from frontend.ui.mn_wd import MW
from frontend.ui.tm import TM
from frontend.core.bc import BC

bc_instance = None

def ck_bd():
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    possible_paths = [
        os.path.join(base_dir, "bin", "SPF.exe"),
        os.path.join(base_dir, "frontend", "bin", "SPF.exe")
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return True
    
    try:
        build_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_backend.bat")
        if os.path.exists(build_script):
            subprocess.run(build_script, shell=True, check=True)
            for path in possible_paths:
                if os.path.exists(path):
                    return True
        else:
            logging.error("Build script not found")
            return False
    except Exception as e:
        logging.error(f"Error building backend: {e}")
        return False
    
    return False

def MN():
    global bc_instance
    app = QApplication(sys.argv)
    TM.ap_dk(app)
    
    if not ck_bd():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Backend component not found")
        msg.setInformativeText("The spoofer backend could not be built or found. Some features may not work correctly.")
        msg.setWindowTitle("Warning")
        msg.exec_()
    
    bc_instance = BC()
    window = MW()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    MN() 