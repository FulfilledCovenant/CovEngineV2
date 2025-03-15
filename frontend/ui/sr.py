from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
                                QLabel, QFrame, QSizePolicy)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon
from .tm import TM

class SR(QWidget):

    page_changed = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(200)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(50, 50, 50))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.current_theme = TM.DARK

        self.stUI()
        
    def stUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 20, 0, 20)
        layout.setSpacing(5)

        self.title_label = QLabel("Navigation")
        self.title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet("color: white; padding: 10px;")
        
        layout.addWidget(self.title_label)
        layout.addSpacing(20)

        self.home_btn = self.ce_bn("Home", 0)
        self.dashboard_btn = self.ce_bn("Dashboard", 1)
        self.settings_btn = self.ce_bn("Settings", 2)
        self.system_metrics_btn = self.ce_bn("SystemMetrics", 3)
        self.tweaks_btn = self.ce_bn("Tweaks", 4)

        layout.addWidget(self.home_btn)
        layout.addWidget(self.dashboard_btn)
        layout.addWidget(self.settings_btn)
        layout.addWidget(self.system_metrics_btn)
        layout.addWidget(self.tweaks_btn)

        layout.addStretch()

        self.sp_bd(self.home_btn)
        
    def ce_bn(self, text, page_index):
        button = QPushButton(text)
        button.setMinimumHeight(50)
        button.setCursor(Qt.PointingHandCursor)

        button.setStyleSheet(self.gt_bn(False))

        button.clicked.connect(lambda: self.ce_pe(button, page_index))
        
        return button
    
    def ce_pe(self, button, index):

        for btn in [self.home_btn, self.dashboard_btn, self.settings_btn, 
                    self.system_metrics_btn, self.tweaks_btn]:
            self.rt_bd(btn)

        self.sp_bd(button)

        self.page_changed.emit(index)
    
    def sp_bd(self, button):
        button.setStyleSheet(self.gt_bn(True))
    
    def rt_bd(self, button):
        button.setStyleSheet(self.gt_bn(False))
        
    def gt_bn(self, selected):
        if self.current_theme == TM.DARK:
            if selected:
                return """
                    QPushButton {
                        background-color: #2a82da;
                        color: white;
                        border: none;
                        text-align: left;
                        padding-left: 20px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #3a92ea;
                    }
                    QPushButton:pressed {
                        background-color: #1a72ca;
                    }
                """
            else:
                return """
                    QPushButton {
                        background-color: transparent;
                        color: #cccccc;
                        border: none;
                        text-align: left;
                        padding-left: 20px;
                        font-size: 14px;
                    }
                    QPushButton:hover {
                        background-color: #656565;
                        color: white;
                    }
                    QPushButton:pressed {
                        background-color: #787878;
                    }
                """
        else:  
            if selected:
                return """
                    QPushButton {
                        background-color: #2a82da;
                        color: white;
                        border: none;
                        text-align: left;
                        padding-left: 20px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #3a92ea;
                    }
                    QPushButton:pressed {
                        background-color: #1a72ca;
                    }
                """
            else:
                return """
                    QPushButton {
                        background-color: transparent;
                        color: #444444;
                        border: none;
                        text-align: left;
                        padding-left: 20px;
                        font-size: 14px;
                    }
                    QPushButton:hover {
                        background-color: #e0e0e0;
                        color: black;
                    }
                    QPushButton:pressed {
                        background-color: #cccccc;
                    }
                """
    
    def ud_ss(self, theme_name):

        self.current_theme = theme_name

        if theme_name == TM.DARK:
            self.title_label.setStyleSheet("color: white; padding: 10px;")
        else:
            self.title_label.setStyleSheet("color: #333333; padding: 10px;")

        for btn in [self.home_btn, self.dashboard_btn, self.settings_btn, 
                    self.system_metrics_btn, self.tweaks_btn]:

            if btn.styleSheet().find("background-color: #2a82da") != -1:
                self.sp_bd(btn)
            else:
                self.rt_bd(btn) 