from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QCheckBox,
                               QFrame, QPushButton, QComboBox, QHBoxLayout,
                               QFormLayout, QSpinBox, QGroupBox, QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from .tm import TM

class SE(QWidget):

    theme_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.current_theme = TM.DARK
        self.stUI()

    def stUI(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        header_label = QLabel("Settings")
        header_font = QFont()
        header_font.setPointSize(18)
        header_font.setBold(True)
        header_label.setFont(header_font)

        main_layout.addWidget(header_label)

        app_group = QGroupBox("Application Settings")
        """)

        app_layout = QFormLayout(app_group)
        app_layout.setSpacing(10)

        theme_label = QLabel("Theme:")
        self.theme_combo = QComboBox()
        self.theme_combo.addItems([TM.DARK, TM.LIGHT, TM.SYSTEM])
        self.theme_combo.setCurrentText(self.current_theme)
        self.theme_combo.currentTextChanged.connect(self.ch_te)
        app_layout.addRow(theme_label, self.theme_combo)

        main_layout.addWidget(app_group)

        perf_group = QGroupBox("Performance Settings")
        """)

        perf_layout = QFormLayout(perf_group)
        perf_layout.setSpacing(10)

        monitor_label = QLabel("Monitoring interval (seconds):")
        self.monitor_spin = QSpinBox()
        self.monitor_spin.setRange(1, 60)
        self.monitor_spin.setValue(1)
        perf_layout.addRow(monitor_label, self.monitor_spin)

        main_layout.addWidget(perf_group)

        buttons_layout = QHBoxLayout()

        self.save_btn = QPushButton("Save Settings")
        self.save_btn.setMinimumHeight(30)
        self.save_btn.clicked.connect(self.se_ss)

        self.reset_btn = QPushButton("Reset to Default")
        self.reset_btn.setMinimumHeight(30)
        self.reset_btn.clicked.connect(self.rt_dt)

        buttons_layout.addStretch()
        buttons_layout.addWidget(self.reset_btn)
        buttons_layout.addWidget(self.save_btn)

        main_layout.addLayout(buttons_layout)
        main_layout.addStretch()

    def ch_te(self, theme_name):
        if theme_name != self.current_theme:
            self.current_theme = theme_name
            self.theme_changed.emit(theme_name)

    def se_ss(self):
        settings = {
            "theme": self.theme_combo.currentText(),
            "monitoring_interval": self.monitor_spin.value()
        }

        msg = QMessageBox()
        msg.setWindowTitle("Settings Saved")
        msg.setText("Your settings have been saved successfully.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def rt_dt(self):
        self.theme_combo.setCurrentText(TM.DARK)
        self.monitor_spin.setValue(1)

        if self.current_theme != TM.DARK:
            self.ch_te(TM.DARK)

        msg = QMessageBox()
        msg.setWindowTitle("Settings Reset")
        msg.setText("Settings have been reset to default values.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
