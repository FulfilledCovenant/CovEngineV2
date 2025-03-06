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
        description.setStyleSheet("color: #888888;")
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

            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Tweak Application Results")
        dialog.setMinimumSize(500, 400)

        layout = QVBoxLayout()

        header = QLabel("Tweak Application Results")
        header.setFont(QFont("Segoe UI", 14, QFont.Bold))
        layout.addWidget(header)

        successful_count = len(results.get("successful", []))
        failed_count = len(results.get("failed", []))
        skipped_count = len(results.get("skipped", []))

        summary = QLabel(f"Successfully applied: {successful_count}\nFailed: {failed_count}\nSkipped: {skipped_count}")
        summary.setFont(QFont("Segoe UI", 10))
        layout.addWidget(summary)

        details = QTextEdit()
        details.setReadOnly(True)
        details.setFont(QFont("Consolas", 9))

        details_text = "=== SUCCESSFUL TWEAKS ===\n"
        for tweak in results.get("successful", []):
            details_text += f"✓ {tweak}\n"

        if failed_count > 0:
            details_text += "\n=== FAILED TWEAKS ===\n"
            for failed in results.get("failed", []):
                details_text += f"✗ {failed['id']}: {failed.get('reason', 'Unknown error')}\n"

        if skipped_count > 0:
            details_text += "\n=== SKIPPED TWEAKS ===\n"
            for skipped in results.get("skipped", []):
                if isinstance(skipped, dict):
                    details_text += f"⚠ {skipped['id']}: {skipped.get('reason', 'Unknown reason')}\n"
                else:
                    details_text += f"⚠ {skipped}\n"

        details.setText(details_text)
        layout.addWidget(details)

        if results.get("requires_restart", False):
            restart_notice = QLabel(
                "Some tweaks require a system restart to take effect. "
                "It is recommended to restart your computer now."
            )
            restart_notice.setFont(QFont("Segoe UI", 10))
            restart_notice.setStyleSheet("color: #FF5722; font-weight: bold;")
            restart_notice.setWordWrap(True)
            layout.addWidget(restart_notice)

            restart_button = QPushButton("Restart Now")
            restart_button.setFont(QFont("Segoe UI", 10))
            restart_button.clicked.connect(self.restart_system)
            layout.addWidget(restart_button)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(dialog.accept)
        layout.addWidget(button_box)

        dialog.setLayout(layout)
        dialog.exec_()

    def restart_system(self):
        reply = QMessageBox.question(
            self,
            "Restart System",
            "Your computer will restart in 1 minute to apply the mouse acceleration tweak. Save your work now.",
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Ok
        )

        if reply == QMessageBox.Ok:
            if os.name == 'nt':
                os.system("shutdown /r /t 60 /f /c \"Restarting to apply mouse acceleration tweak\"")
            else:
                os.system("sudo shutdown -r +1 \"Restarting to apply mouse acceleration tweak\"")
