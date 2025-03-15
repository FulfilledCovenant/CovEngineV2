from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette
from .tm import TM

class HR(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(50)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(40, 40, 40))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.current_theme = TM.DARK

        self.stUI()
        
    def stUI(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 0, 20, 0)

        self.title_label = QLabel("CovEngineV2")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet("color: white;")

        self.creator_label = QLabel("filefilza - fulfilledcovenant")
        creator_font = QFont()
        creator_font.setPointSize(10)
        self.creator_label.setFont(creator_font)
        self.creator_label.setStyleSheet("color: #cccccc;")

        layout.addWidget(self.title_label)
        layout.addStretch()
        layout.addWidget(self.creator_label)
        
    def ud_ss(self, theme_name):
        self.current_theme = theme_name
        
        if theme_name == TM.DARK:

            self.title_label.setStyleSheet("color: white;")
            self.creator_label.setStyleSheet("color: #cccccc;")

            palette = self.palette()
            palette.setColor(QPalette.Window, QColor(40, 40, 40))
            self.setPalette(palette)
        else:

            self.title_label.setStyleSheet("color: #333333;")
            self.creator_label.setStyleSheet("color: #555555;")

            palette = self.palette()
            palette.setColor(QPalette.Window, QColor(230, 230, 230))
            self.setPalette(palette) 