from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                               QTabWidget, QLabel, QSpacerItem, QSizePolicy,
                               QMessageBox, QProgressDialog, QScrollArea, QCheckBox,
                               QDialog, QTextEdit, QDialogButtonBox, QGroupBox, QGridLayout)
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication
import os
import sys
import json
import logging
from typing import Dict, List, Any, Optional

from frontend.ui.gl_st import GS  
from frontend.ui.tweaks.tw_pe import PE
from frontend.ui.tweaks.tw_ge import GE
from frontend.ui.tweaks.tw_py import PY
from frontend.ui.tweaks.tw_sy import SY
from frontend.core.tw_mg import TM

class TS(QWidget):
    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.logger = logging.getLogger("TweaksPage")
        self.tweak_manager = TM()
        self.selected_tweaks = {}
        self.init_ui()
        
    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        header_layout = QHBoxLayout()
        
        title_label = QLabel("System Tweaks")
        title_label.setFont(QFont("Segoe UI", 18, QFont.Bold))
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()

        self.apply_button = QPushButton("Apply Selected Tweaks")
        self.apply_button.setMinimumSize(QSize(180, 40))
        self.apply_button.setFont(QFont("Segoe UI", 10))
        GS.apply_button_style(self.apply_button)
        self.apply_button.clicked.connect(self.apply_selected_tweaks)
        header_layout.addWidget(self.apply_button)
        
        main_layout.addLayout(header_layout)

        description = QLabel(
            "Select tweaks to optimize your system. Each tweak can improve performance, "
            "gaming experience, privacy, or security. Use caution when applying tweaks as "
            "some may require a system restart or may not be suitable for all systems."
        )
        description.setWordWrap(True)
        description.setFont(QFont("Segoe UI", 10))
        description.setStyleSheet("color: 888888;")
        main_layout.addWidget(description)

        self.tabs = QTabWidget()
        self.tabs.setFont(QFont("Segoe UI", 10))

        self.performance_tab = PE()
        self.tabs.addTab(self.performance_tab, "Performance")
        
        self.gaming_tab = GE()
        self.tabs.addTab(self.gaming_tab, "Gaming")
        
        self.privacy_tab = PY()
        self.tabs.addTab(self.privacy_tab, "Privacy")
        
        self.security_tab = SY()
        self.tabs.addTab(self.security_tab, "Security")
        
        main_layout.addWidget(self.tabs)

        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.setContentsMargins(10, 10, 10, 10)

        self.select_all_btn = QPushButton("Select All")
        self.select_all_btn.setFont(QFont("Segoe UI", 10))
        GS.apply_button_style(self.select_all_btn, secondary=True)
        self.select_all_btn.clicked.connect(self.select_all_tweaks)

        self.deselect_all_btn = QPushButton("Deselect All")
        self.deselect_all_btn.setFont(QFont("Segoe UI", 10))
        GS.apply_button_style(self.deselect_all_btn, secondary=True)
        self.deselect_all_btn.clicked.connect(self.deselect_all_tweaks)

        button_layout.addWidget(self.select_all_btn)
        button_layout.addWidget(self.deselect_all_btn)
        button_layout.addStretch()
        
        main_layout.addWidget(button_container)
        
        self.setLayout(main_layout)
        
    def select_all_tweaks(self):
        current_tab = self.tabs.currentWidget()
        for checkbox in current_tab.findChildren(QCheckBox):
            checkbox.setChecked(True)
    
    def deselect_all_tweaks(self):
        current_tab = self.tabs.currentWidget()
        for checkbox in current_tab.findChildren(QCheckBox):
            checkbox.setChecked(False)
    
    def get_selected_tweaks(self):
        selected_tweaks = {
            "performance": [],
            "gaming": [],
            "privacy": [],
            "security": []
        }

        for checkbox in self.performance_tab.findChildren(QCheckBox):
            if checkbox.isChecked():
                tweak_id = checkbox.property("tweak_id")
                if tweak_id:
                    selected_tweaks["performance"].append(tweak_id)

        for checkbox in self.gaming_tab.findChildren(QCheckBox):
            if checkbox.isChecked():
                tweak_id = checkbox.property("tweak_id")
                if tweak_id:
                    selected_tweaks["gaming"].append(tweak_id)

        for checkbox in self.privacy_tab.findChildren(QCheckBox):
            if checkbox.isChecked():
                tweak_id = checkbox.property("tweak_id")
                if tweak_id:
                    selected_tweaks["privacy"].append(tweak_id)

        for checkbox in self.security_tab.findChildren(QCheckBox):
            if checkbox.isChecked():
                tweak_id = checkbox.property("tweak_id")
                if tweak_id:
                    selected_tweaks["security"].append(tweak_id)

        for category in list(selected_tweaks.keys()):
            if not selected_tweaks[category]:
                del selected_tweaks[category]
                
        return selected_tweaks
    
    def apply_selected_tweaks(self):

        selected_tweaks = self.get_selected_tweaks()

        if not selected_tweaks:
            QMessageBox.information(
                self,
                "No Tweaks Selected",
                "Please select at least one tweak to apply."
            )
            return

        total_tweaks = sum(len(tweaks) for tweaks in selected_tweaks.values())
        
        onedrive_selected = False
        for category, tweaks in selected_tweaks.items():
            if "disable_onedrive" in tweaks:
                onedrive_selected = True
                break
                
        if onedrive_selected:
            onedrive_warning = QMessageBox()
            onedrive_warning.setWindowTitle("OneDrive Warning")
            onedrive_warning.setText("Warning: You are about to disable OneDrive")
            onedrive_warning.setInformativeText(
                "This tweak will disable and uninstall Microsoft OneDrive.\n\n"
                "If you have files or folders stored in OneDrive, you may lose access to them.\n"
                "Please ensure all your OneDrive files are synced to your local device before proceeding.\n\n"
                "Do you want to continue with disabling OneDrive?"
            )
            onedrive_warning.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            onedrive_warning.setDefaultButton(QMessageBox.No)
            onedrive_warning.setIcon(QMessageBox.Critical)
            
            if onedrive_warning.exec_() != QMessageBox.Yes:
                for category in selected_tweaks:
                    if "disable_onedrive" in selected_tweaks[category]:
                        selected_tweaks[category].remove("disable_onedrive")
                        
                total_tweaks = sum(len(tweaks) for tweaks in selected_tweaks.values())
                if total_tweaks == 0:
                    QMessageBox.information(
                        self,
                        "No Tweaks Selected",
                        "No tweaks left to apply after removing OneDrive tweak."
                    )
                    return

        msg = QMessageBox()
        msg.setWindowTitle("Confirm Tweak Application")
        msg.setText(f"You are about to apply {total_tweaks} tweaks to your system.")
        msg.setInformativeText(
            "A system restore point will be created before applying tweaks for safety.\n\n"
            "Some tweaks may require a system restart to take effect.\n"
            "Do you want to continue?"
        )
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.setIcon(QMessageBox.Warning)
        
        if msg.exec_() != QMessageBox.Yes:
            return

        progress = QProgressDialog("Creating system restore point...", "Cancel", 0, total_tweaks + 1, self)
        progress.setWindowTitle("Applying Tweaks")
        progress.setWindowModality(Qt.WindowModal)
        progress.setMinimumDuration(0)
        progress.setValue(0)

        restore_result = self.tweak_manager.ce_rp()
        
        if not restore_result.get("success", False):

            warning = QMessageBox()
            warning.setWindowTitle("Restore Point Warning")
            warning.setText("Failed to create system restore point.")
            warning.setInformativeText(
                "The system restore point could not be created. This may be due to insufficient disk space "
                "or system protection settings.\n\n"
                "Do you still want to continue applying tweaks without a restore point?"
            )
            warning.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            warning.setDefaultButton(QMessageBox.No)
            warning.setIcon(QMessageBox.Warning)
            
            if warning.exec_() != QMessageBox.Yes:
                progress.cancel()
                return

        progress.setValue(1)
        progress.setLabelText("Applying tweaks...")

        results = self.tweak_manager.ay_ts(selected_tweaks, create_restore_point=False)  

        progress.setValue(total_tweaks + 1)

        self.show_results_dialog(results)
        
    def show_results_dialog(self, results: Dict[str, Any]):

        if "disable_mouse_acceleration" in results.get("successful", []):

            msg = QMessageBox()
            msg.setWindowTitle("System Restart Required")
            msg.setText("Mouse Acceleration Tweak Applied")
            msg.setInformativeText(
                "The mouse acceleration tweak requires a system restart to take effect.\n\n"
                "Your computer will restart in 1 minute.\n"
                "Please save all your work now."
            )
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            if os.name == 'nt':
                os.system("shutdown /r /t 60 /f /c \"Restarting to apply mouse acceleration tweak\"")
            else:
                os.system("sudo shutdown -r +1 \"Restarting to apply mouse acceleration tweak\"") 