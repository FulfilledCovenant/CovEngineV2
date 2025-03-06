from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                               QStackedWidget, QLabel, QSpacerItem, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup
from PyQt5.QtGui import QFont, QIcon, QColor, QPalette

from frontend.ui.pe_de import DE
from frontend.ui.pe_sm import SM
from frontend.ui.pe_se import SE
from frontend.ui.pe_ts import TS
from frontend.ui.hr import HR
from frontend.ui.pe_he import HE
from frontend.ui.gl_st import GS, GW

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CovEngineV2")
        self.setGeometry(100, 100, 1200, 800)
        self.setMinimumSize(1000, 700)

        """)

        self.animations = []

        self.stUI()

    def stUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        sidebar = self.cr_sb()

        content_container = QWidget()
        """)
        content_layout = QVBoxLayout(content_container)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        header = self.cr_hr()
        content_layout.addWidget(header)

        self.stacked_widget = QStackedWidget()
        content_layout.addWidget(self.stacked_widget)

        self.ie_ps()

        main_layout.addWidget(sidebar, 1)
        main_layout.addWidget(content_container, 5)

        self.cr_cs()

    def cr_sb(self):
        sidebar = QWidget()
        """)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(15, 25, 15, 25)
        sidebar_layout.setSpacing(15)

        title_label = QLabel("CovEngine")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background-color: transparent;")
        title_label.setAlignment(Qt.AlignCenter)

        version_label = QLabel("v2.0")
        version_label.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']}; background-color: transparent;")
        version_label.setAlignment(Qt.AlignCenter)

        sidebar_layout.addWidget(title_label)
        sidebar_layout.addWidget(version_label)
        sidebar_layout.addSpacing(30)

        self.nav_buttons = {}


        home_btn = QPushButton("Home")
        home_btn.setObjectName("home")
        home_btn.setStyleSheet(button_style)

        dashboard_btn = QPushButton("Dashboard")
        dashboard_btn.setObjectName("dashboard")
        dashboard_btn.setStyleSheet(button_style)

        metrics_btn = QPushButton("System Metrics")
        metrics_btn.setObjectName("metrics")
        metrics_btn.setStyleSheet(button_style)

        tweaks_btn = QPushButton("Tweaks")
        tweaks_btn.setObjectName("tweaks")
        tweaks_btn.setStyleSheet(button_style)

        settings_btn = QPushButton("Settings")
        settings_btn.setObjectName("settings")
        settings_btn.setStyleSheet(button_style)

        self.nav_buttons = {
            "home": home_btn,
            "dashboard": dashboard_btn,
            "metrics": metrics_btn,
            "tweaks": tweaks_btn,
            "settings": settings_btn
        }

        sidebar_layout.addWidget(home_btn)
        sidebar_layout.addWidget(dashboard_btn)
        sidebar_layout.addWidget(metrics_btn)
        sidebar_layout.addWidget(tweaks_btn)
        sidebar_layout.addSpacing(20)
        sidebar_layout.addWidget(settings_btn)

        sidebar_layout.addStretch()

        return sidebar

    def cr_hr(self):
        header = QWidget()
        header.setFixedHeight(60)
        """)

        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 0, 20, 0)

        self.page_title = QLabel("Home")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        self.page_title.setFont(title_font)
        self.page_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background-color: transparent;")

        header_layout.addWidget(self.page_title)
        header_layout.addStretch()

        return header

    def ie_ps(self):
        self.home_page = HE(self)
        self.stacked_widget.addWidget(self.home_page)

        self.dashboard_page = DE()
        self.stacked_widget.addWidget(self.dashboard_page)

        self.metrics_page = SM()
        self.stacked_widget.addWidget(self.metrics_page)

        self.tweaks_page = TS(self)
        self.stacked_widget.addWidget(self.tweaks_page)

        self.settings_page = SE()
        self.stacked_widget.addWidget(self.settings_page)

    def cr_cs(self):
        self.nav_buttons["home"].clicked.connect(lambda: self.ce_pe("home", 0))
        self.nav_buttons["dashboard"].clicked.connect(lambda: self.ce_pe("dashboard", 1))
        self.nav_buttons["metrics"].clicked.connect(lambda: self.ce_pe("metrics", 2))
        self.nav_buttons["tweaks"].clicked.connect(lambda: self.ce_pe("tweaks", 3))
        self.nav_buttons["settings"].clicked.connect(lambda: self.ce_pe("settings", 4))

    def ce_pe(self, page_name, index):
        self.page_title.setText(page_name.capitalize())

        for key, btn in self.nav_buttons.items():
            if key == page_name:
                btn.setObjectName("active")
            else:
                btn.setObjectName(key)
            btn.style().unpolish(btn)
            btn.style().polish(btn)

        self.stacked_widget.setCurrentIndex(index)

        if page_name == "metrics":
            self.metrics_page.rf_dt()

    def ay_fe(self, widget):
        pass

    def ch_te(self):
        QMessageBox.information(self, "Theme Toggle", "Theme toggling is currently disabled.")

    def ud_ss(self):
        pass
