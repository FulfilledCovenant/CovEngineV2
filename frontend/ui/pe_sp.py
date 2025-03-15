import os
import json
import logging
import subprocess
import time
import sys
import ctypes
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, 
    QLabel, QPushButton, QGroupBox, QMessageBox,
    QProgressBar, QGridLayout, QFrame
)
from PyQt5.QtCore import Qt, QSize, QTimer, QPropertyAnimation, QEasingCurve, QRect
from PyQt5.QtGui import QFont, QColor, QPalette, QMovie

from frontend.ui.gl_st import GS

class SP(QScrollArea):
    
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("SpoofTab")
        self.init_ui()
        
    def init_ui(self):
        self.setWidgetResizable(True)
        self.setFrameShape(QScrollArea.NoFrame)
        
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        header_layout = QHBoxLayout()
        layout.addLayout(header_layout)
        
        title = QLabel("System Spoofer")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']};")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        desc = QLabel("Spoof your system to prevent detection")
        desc.setFont(QFont("Segoe UI", 11))
        desc.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']};")
        desc.setAlignment(Qt.AlignLeft)
        desc.setContentsMargins(0, 5, 0, 15)
        layout.addWidget(desc)
        
        main_content = QHBoxLayout()
        layout.addLayout(main_content)
        
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 20, 0)
        left_layout.setSpacing(15)
        
        spoof_group = QGroupBox("Spoof")
        spoof_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                font-size: 13px;
                color: {GS.DARK_THEME['text_primary']};
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 5px 0 5px;
            }}
        """)
        spoof_layout = QVBoxLayout()
        spoof_layout.setContentsMargins(15, 25, 15, 15)
        spoof_layout.setSpacing(20)
        
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(15)
        
        self.launch_btn = QPushButton("Launch")
        self.launch_btn.setMinimumSize(QSize(180, 50))
        self.launch_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.launch_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {GS.DARK_THEME['accent']};
                color: white;
                border-radius: 6px;
                padding: 10px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {GS.DARK_THEME['accent_hover']};
            }}
            QPushButton:pressed {{
                background-color: {GS.DARK_THEME['accent']};
            }}
        """)
        self.launch_btn.clicked.connect(self.lc_sf)
        buttons_layout.addWidget(self.launch_btn, 0, Qt.AlignCenter)
        
        self.ud_launch_btn = QPushButton("UD Temp Spoof")
        self.ud_launch_btn.setMinimumSize(QSize(180, 50))
        self.ud_launch_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.ud_launch_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {GS.DARK_THEME['accent']};
                color: white;
                border-radius: 6px;
                padding: 10px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {GS.DARK_THEME['accent_hover']};
            }}
            QPushButton:pressed {{
                background-color: {GS.DARK_THEME['accent']};
            }}
        """)
        self.ud_launch_btn.clicked.connect(self.lc_ud_sf)
        buttons_layout.addWidget(self.ud_launch_btn, 0, Qt.AlignCenter)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setStyleSheet(f"""
            QProgressBar {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                border-radius: 4px;
                text-align: center;
                height: 20px;
                color: white;
            }}
            QProgressBar::chunk {{
                background-color: {GS.DARK_THEME['accent']};
                border-radius: 4px;
            }}
        """)
        
        self.status_label = QLabel("")
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']};")
        
        spoof_layout.addLayout(buttons_layout)
        spoof_layout.addWidget(self.progress_bar)
        spoof_layout.addWidget(self.status_label)
        spoof_layout.addStretch()
        
        spoof_group.setLayout(spoof_layout)
        left_layout.addWidget(spoof_group)
        
        self.animate_container = QWidget()
        self.animate_container.setStyleSheet(f"""
            background-color: {GS.DARK_THEME['bg_tertiary']};
            border-radius: 8px;
        """)
        animate_layout = QVBoxLayout(self.animate_container)
        animate_layout.setContentsMargins(15, 15, 15, 15)
        
        self.animation_label = QLabel()
        self.animation_label.setAlignment(Qt.AlignCenter)
        animate_layout.addWidget(self.animation_label)
        
        left_layout.addWidget(self.animate_container)
        
        self.st_ai()
        
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(15)
        
        warning_group = QGroupBox("Warning")
        warning_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                font-size: 13px;
                color: {GS.DARK_THEME['text_primary']};
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 5px 0 5px;
            }}
        """)
        warning_layout = QVBoxLayout()
        warning_layout.setContentsMargins(15, 15, 15, 15)
        
        warning_text = QLabel("Do not launch, if you have the following games, and its processes open: Fortnite, Valorant, R6")
        warning_text.setWordWrap(True)
        warning_text.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']};")
        warning_text.setFont(QFont("Segoe UI", 10))
        warning_layout.addWidget(warning_text)
        
        warning_group.setLayout(warning_layout)
        right_layout.addWidget(warning_group)
        
        info_group = QGroupBox("Information")
        info_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: bold;
                font-size: 13px;
                color: {GS.DARK_THEME['text_primary']};
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 8px;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 12px;
                padding: 0 5px 0 5px;
            }}
        """)
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(15, 15, 15, 15)
        info_layout.setSpacing(10)
        
        info_text = QLabel(
            "The spoofer will temporarily modify system identifiers to prevent tracking. "
            "This is done by loading a driver that masks hardware identifiers. "
            "The process will automatically clean up after itself."
        )
        info_text.setWordWrap(True)
        info_text.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']};")
        info_text.setFont(QFont("Segoe UI", 10))
        info_layout.addWidget(info_text)
        
        hw_ids_frame = QFrame()
        hw_ids_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {GS.DARK_THEME['bg_tertiary']};
                border-radius: 6px;
            }}
        """)
        hw_ids_layout = QVBoxLayout(hw_ids_frame)
        hw_ids_layout.setContentsMargins(15, 15, 15, 15)
        hw_ids_layout.setSpacing(10)
        
        hw_ids_header = QHBoxLayout()
        hw_ids_title = QLabel("System Identifiers")
        hw_ids_title.setFont(QFont("Segoe UI", 11, QFont.Bold))
        hw_ids_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']};")
        hw_ids_header.addWidget(hw_ids_title)
        
        hw_ids_header.addStretch()
        
        refresh_btn = QPushButton("Refresh")
        refresh_btn.setFixedSize(80, 30)
        refresh_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {GS.DARK_THEME['bg_secondary']};
                color: {GS.DARK_THEME['text_primary']};
                border-radius: 4px;
                padding: 5px;
            }}
            QPushButton:hover {{
                background-color: {GS.DARK_THEME['accent']};
                color: white;
            }}
        """)
        refresh_btn.clicked.connect(self.gt_si)
        hw_ids_header.addWidget(refresh_btn)
        
        hw_ids_layout.addLayout(hw_ids_header)
        
        hw_ids_grid = QGridLayout()
        hw_ids_grid.setColumnStretch(1, 1)
        hw_ids_grid.setHorizontalSpacing(15)
        hw_ids_grid.setVerticalSpacing(8)
        
        self.hw_labels = {}
        
        hw_ids = [
            ("cpu_serial", "CPU Serial:"),
            ("smbios_serial", "smBIOS Serial:"),
            ("mb_serial", "Motherboard Serial:"),
            ("uuid", "UUID:"),
            ("mac_address", "MAC Address:"),
            ("tpm_status", "TPM Status:"),
            ("disk_hwid", "Disk HWID:")
        ]
        
        for row, (key, label) in enumerate(hw_ids):
            label_widget = QLabel(label)
            label_widget.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']};")
            label_widget.setFont(QFont("Segoe UI", 9))
            
            value_widget = QLabel("Loading...")
            value_widget.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']};")
            value_widget.setFont(QFont("Segoe UI", 9))
            value_widget.setTextInteractionFlags(Qt.TextSelectableByMouse)
            
            hw_ids_grid.addWidget(label_widget, row, 0)
            hw_ids_grid.addWidget(value_widget, row, 1)
            
            self.hw_labels[key] = value_widget
        
        hw_ids_layout.addLayout(hw_ids_grid)
        info_layout.addWidget(hw_ids_frame)
        
        info_group.setLayout(info_layout)
        right_layout.addWidget(info_group)
        
        right_layout.addStretch()
        
        main_content.addWidget(left_widget, 1)
        main_content.addWidget(right_widget, 1)
        
        self.setWidget(content)
        
        QTimer.singleShot(100, self.gt_si)
        
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
            
    def gt_si(self):
        for key in self.hw_labels:
            self.hw_labels[key].setText("Loading...")
            
        QTimer.singleShot(100, self.ft_si)
        
    def ft_si(self):
        try:
            disk_info = self.ge_cd("wmic diskdrive get model, serialnumber")
            self.hw_labels["disk_hwid"].setText(self.px_cm(disk_info, start_line=1))
            
            cpu_info = self.ge_cd("wmic cpu get serialnumber")
            self.hw_labels["cpu_serial"].setText(self.px_cm(cpu_info, start_line=1))
            
            bios_info = self.ge_cd("wmic bios get serialnumber")
            self.hw_labels["smbios_serial"].setText(self.px_cm(bios_info, start_line=1))
            
            mb_info = self.ge_cd("wmic baseboard get serialnumber")
            self.hw_labels["mb_serial"].setText(self.px_cm(mb_info, start_line=1))
            
            uuid_info = self.ge_cd("wmic path win32_computersystemproduct get uuid")
            self.hw_labels["uuid"].setText(self.px_cm(uuid_info, start_line=1))
            
            mac_info = self.ge_cd("getmac /v /fo list | findstr Physical")
            self.hw_labels["mac_address"].setText(self.px_cm(mac_info).split(":")[-1].strip() if mac_info else "N/A")
            
            tpm_info = self.ge_cd("wmic /namespace:\\\\root\\CIMV2\\Security\\MicrosoftTpm path Win32_Tpm get IsEnabled_InitialValue")
            tpm_value = self.px_cm(tpm_info, start_line=1)
            tpm_status = "Enabled" if tpm_value and tpm_value.strip() == "TRUE" else "Disabled"
            self.hw_labels["tpm_status"].setText(tpm_status)
        except Exception as e:
            self.logger.error(f"Error fetching system identifiers: {e}")
            for key in self.hw_labels:
                if self.hw_labels[key].text() == "Loading...":
                    self.hw_labels[key].setText("Error fetching data")
    
    def ge_cd(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout.strip() if result.returncode == 0 else ""
        except Exception:
            return ""
    
    def px_cm(self, output, start_line=0):
        if not output:
            return "N/A"
        lines = [line.strip() for line in output.splitlines() if line.strip()]
        if len(lines) <= start_line:
            return "N/A"
        return lines[start_line]
        
    def st_ai(self):
        self.animate_btn = QPushButton("pulse", self.animate_container)
        self.animate_btn.setGeometry(10, 10, 20, 20)
        self.animate_btn.setStyleSheet(f"background-color: {GS.DARK_THEME['accent']}; border-radius: 10px; border: none;")
        self.animate_btn.setVisible(True)
        
        self.animation = QPropertyAnimation(self.animate_btn, b"geometry")
        self.animation.setDuration(1500)
        self.animation.setStartValue(QRect(50, 50, 20, 20))
        self.animation.setEndValue(QRect(150, 50, 60, 60))
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.rv_ai)
        self.animation.start()
        
    def rv_ai(self):
        self.animation.setStartValue(QRect(150, 50, 60, 60))
        self.animation.setEndValue(QRect(50, 50, 20, 20))
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.st_ai)
        self.animation.start()
        
    def lc_sf(self):
        if not self.ck_bd_ex():
            QMessageBox.warning(
                self, 
                "Backend Not Found", 
                "The backend executable (SPF.exe) was not found.\nPlease rebuild the application."
            )
            return
            
        result = self.ck_rg()
        if result != "No blocked games running":
            QMessageBox.warning(
                self, 
                "Warning", 
                f"{result} detected. Please close it before proceeding."
            )
            return
        
        reply = QMessageBox.question(
            self, 
            "Confirmation", 
            "Are you sure you want to proceed with spoofing? This will require administrator privileges.",
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.launch_btn.setEnabled(False)
            self.ud_launch_btn.setEnabled(False)
            self.progress_bar.setVisible(True)
            self.status_label.setText("Starting spoof process...")
            self.rn_sf("spoof")
    
    def lc_ud_sf(self):
        if not self.ck_bd_ex():
            QMessageBox.warning(
                self, 
                "Backend Not Found", 
                "The backend executable (SPF.exe) was not found.\nPlease rebuild the application."
            )
            return
            
        result = self.ck_rg()
        if result != "No blocked games running":
            QMessageBox.warning(
                self, 
                "Warning", 
                f"{result} detected. Please close it before proceeding."
            )
            return
        
        reply = QMessageBox.question(
            self, 
            "Confirmation", 
            "Are you sure you want to proceed with UD Temp spoofing? This will require administrator privileges.",
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.launch_btn.setEnabled(False)
            self.ud_launch_btn.setEnabled(False)
            self.progress_bar.setVisible(True)
            self.status_label.setText("Starting UD Temp spoof process...")
            self.rn_sf("udspoof")
    
    def ck_bd_ex(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        possible_paths = [
            os.path.join(base_dir, "bin", "SPF.exe"),
            os.path.join(base_dir, "frontend", "bin", "SPF.exe")
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                self.backend_path = path
                return True
        
        return False
        
    def ck_rg(self):
        try:
            if not hasattr(self, 'backend_path'):
                if not self.ck_bd_ex():
                    return "Backend not found"
            
            result = subprocess.run(
                [self.backend_path, "check"], 
                capture_output=True, 
                text=True, 
                check=False
            )
            
            return result.stdout.strip()
        except Exception as e:
            self.logger.error(f"Error checking running games: {e}")
            return "Error checking games"
            
    def rn_sf(self, command="spoof"):
        try:
            if not hasattr(self, 'backend_path'):
                if not self.ck_bd_ex():
                    raise Exception("Backend executable not found")
            
            self.progress_bar.setValue(10)
            self.status_label.setText(f"Starting backend process for {command}...")
            
            process = subprocess.Popen(
                [self.backend_path, command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            self.spoof_command = command
            self.process = process
            QTimer.singleShot(200, self.ck_ps)
            
        except Exception as e:
            self.logger.error(f"Error in spoof process: {e}")
            self.status_label.setText(f"Error: {str(e)}")
            self.progress_bar.setValue(0)
            self.launch_btn.setEnabled(True)
            self.ud_launch_btn.setEnabled(True)
    
    def ck_ps(self):
        if self.process.poll() is not None:
            stdout, stderr = self.process.communicate()
            
            if self.process.returncode == 0:
                self.progress_bar.setValue(100)
                if self.spoof_command == "udspoof":
                    self.status_label.setText("UD Temp Spoof completed successfully!")
                else:
                    self.status_label.setText("Spoof completed successfully!")
                QTimer.singleShot(2000, self.rst_ui)
            else:
                self.logger.error(f"Backend process failed: {stderr}")
                self.status_label.setText(f"Error: {stderr}")
                self.progress_bar.setValue(0)
                self.launch_btn.setEnabled(True)
                self.ud_launch_btn.setEnabled(True)
        else:
            line = self.ns_ol()
            if line:
                if "Downloading driver" in line or "Downloading UD driver" in line:
                    self.progress_bar.setValue(20)
                    self.status_label.setText("Downloading driver...")
                elif "Downloading mapper" in line or "Downloading UD mapper" in line:
                    self.progress_bar.setValue(40)
                    self.status_label.setText("Downloading mapper...")
                elif "Mapping driver" in line or "Mapping UD driver" in line:
                    self.progress_bar.setValue(60)
                    self.status_label.setText("Mapping driver with administrator privileges...")
                elif "Stopping WMI" in line:
                    self.progress_bar.setValue(80)
                    self.status_label.setText("Stopping WMI service...")
                elif "Cleaning up" in line:
                    self.progress_bar.setValue(90)
                    self.status_label.setText("Cleaning up...")
            
            QTimer.singleShot(200, self.ck_ps)
    
    def ns_ol(self):
        try:
            if hasattr(self, 'process') and self.process.stdout:
                return self.process.stdout.readline().strip()
        except Exception:
            pass
        return ""
        
    def rst_ui(self):
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)
        self.launch_btn.setEnabled(True)
        self.ud_launch_btn.setEnabled(True)
        self.status_label.setText("")
        QTimer.singleShot(500, self.gt_si) 