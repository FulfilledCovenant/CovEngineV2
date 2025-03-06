import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication
from frontend.ui.mn_wd import MW
from frontend.ui.tm import TM
from frontend.core.bc import BC

bc_instance = None

def MN():
    global bc_instance

    app = QApplication(sys.argv)

    TM.ap_dk(app)

    bc_instance = BC()

    window = MW()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    MN()
