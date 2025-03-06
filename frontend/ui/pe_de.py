from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QHBoxLayout,
                               QFrame, QProgressBar, QGridLayout, QScrollArea)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
import psutil
import time
from datetime import datetime

from frontend.ui.gl_st import GS, GW

class DE(QWidget):
    def __init__(self):
        super().__init__()

        self.tt_ug = 0
        self.pc_ct = 0
        self.gm_se = 0

        self.stUI()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ud_ms)
        self.timer.start(3000)

        self.last_update_time = 0

    def stUI(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setStyleSheet("background-color: transparent;")

        scroll_content = QWidget()
        scroll_content.setStyleSheet("background-color: transparent;")
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(25, 25, 25, 25)
        scroll_layout.setSpacing(20)

        header_container = QWidget()
        header_container.setStyleSheet(f"background-color: {GS.DARK_THEME['bg_tertiary']}; border-radius: 10px;")
        header_layout = QVBoxLayout(header_container)
        header_layout.setContentsMargins(20, 20, 20, 20)

        header_label = QLabel("Performance Dashboard")
        header_font = QFont()
        header_font.setPointSize(18)
        header_font.setBold(True)
        header_label.setFont(header_font)
        header_label.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background-color: transparent;")

        self.time_label = QLabel()
        self.time_label.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']}; background-color: transparent;")
        self.ud_te()

        header_layout.addWidget(header_label)
        header_layout.addWidget(self.time_label)

        scroll_layout.addWidget(header_container)

        overview_container = QWidget()
        overview_container.setStyleSheet(f"background-color: {GS.DARK_THEME['bg_tertiary']}; border-radius: 10px;")
        overview_layout = QVBoxLayout(overview_container)
        overview_layout.setContentsMargins(20, 20, 20, 20)

        overview_title = QLabel("System Overview")
        overview_title.setFont(QFont("", 16, QFont.Bold))
        overview_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background-color: transparent;")
        overview_layout.addWidget(overview_title)
        overview_layout.addSpacing(10)

        metrics_layout = QGridLayout()
        metrics_layout.setSpacing(20)
        metrics_layout.setContentsMargins(0, 0, 0, 0)

        self.usage_frame = self.ce_mc("Total System Usage", "0%", GS.DARK_THEME["info"])
        metrics_layout.addWidget(self.usage_frame, 0, 0)

        self.process_frame = self.ce_mc("Process Count", "0", GS.DARK_THEME["accent"])
        metrics_layout.addWidget(self.process_frame, 0, 1)

        overview_layout.addLayout(metrics_layout)

        scroll_layout.addWidget(overview_container)

        score_container = QWidget()
        score_container.setStyleSheet(f"background-color: {GS.DARK_THEME['bg_tertiary']}; border-radius: 10px;")
        score_layout = QVBoxLayout(score_container)
        score_layout.setContentsMargins(20, 20, 20, 20)

        score_title = QLabel("Gaming Performance Score")
        score_title.setFont(QFont("", 16, QFont.Bold))
        score_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background-color: transparent;")
        score_layout.addWidget(score_title)
        score_layout.addSpacing(10)

        score_content_layout = QHBoxLayout()
        score_content_layout.setContentsMargins(0, 0, 0, 0)
        score_content_layout.setSpacing(20)

        self.score_frame = self.ce_mc("Performance Score", "0%", GS.DARK_THEME["success"])
        score_content_layout.addWidget(self.score_frame)

        score_desc_layout = QVBoxLayout()
        score_desc_layout.setContentsMargins(0, 0, 0, 0)
        score_desc_layout.setSpacing(10)

        self.score_desc = QLabel("Calculating your gaming performance score...")
        self.score_desc.setWordWrap(True)
        self.score_desc.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']}; background-color: transparent;")

        criteria_label = QLabel("Score Criteria: <120 processes = Excellent, <200 processes = Good")
        criteria_label.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']}; font-size: 11px; background-color: transparent;")

        score_desc_layout.addWidget(self.score_desc)
        score_desc_layout.addWidget(criteria_label)
        score_desc_layout.addStretch()

        score_content_layout.addLayout(score_desc_layout)
        score_layout.addLayout(score_content_layout)

        scroll_layout.addWidget(score_container)

        scroll_layout.addStretch()

        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

    def ud_te(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.setText(f"Last Updated: {formatted_time}")

    def ce_mc(self, title, value, color):
        frame = QWidget()
        """)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']}; background-color: transparent;")
        layout.addWidget(title_label)

        value_label = QLabel(value)
        value_label.setObjectName(f"{title.lower().replace(' ', '_')}_value")
        value_label.setStyleSheet(f"color: {color}; font-size: 24px; font-weight: bold; background-color: transparent;")
        layout.addWidget(value_label)

        progress = QProgressBar()
        progress.setObjectName(f"{title.lower().replace(' ', '_')}_bar")
        progress.setRange(0, 100)
        progress.setValue(0)
        progress.setTextVisible(False)
        progress.setFixedHeight(6)
        """)
        layout.addWidget(progress)

        return frame

    def ud_ms(self):
        try:
            current_time = time.time()
            if current_time - self.last_update_time < 2.5:
                return

            self.ud_te()

            cpu_usage = psutil.cpu_percent(interval=None)
            memory = psutil.virtual_memory()
            memory_usage = memory.percent

            self.tt_ug = int((cpu_usage + memory_usage) / 2)

            self.pc_ct = len(psutil.pids())

            if self.pc_ct < 120:
                self.gm_se = 95
                score_color = GS.DARK_THEME["success"]
                score_message = "Excellent! Your system has minimal background processes for optimal gaming."
            elif self.pc_ct < 200:
                self.gm_se = 80
                score_color = GS.DARK_THEME["info"]
                score_message = "Good performance. Your system has a reasonable number of processes running."
            elif self.pc_ct < 250:
                self.gm_se = 65
                score_color = GS.DARK_THEME["warning"]
                score_message = "Average performance. Consider closing unnecessary applications."
            else:
                self.gm_se = 50
                score_color = GS.DARK_THEME["error"]
                score_message = "Too many processes are running. Close unnecessary applications for better gaming performance."

            usage_value = self.findChild(QLabel, "total_system_usage_value")
            usage_bar = self.findChild(QProgressBar, "total_system_usage_bar")
            if usage_value and usage_bar:
                usage_value.setText(f"{self.tt_ug}%")
                usage_bar.setValue(self.tt_ug)

            process_value = self.findChild(QLabel, "process_count_value")
            process_bar = self.findChild(QProgressBar, "process_count_bar")
            if process_value and process_bar:
                process_value.setText(f"{self.pc_ct}")
                process_percentage = min(int(self.pc_ct / 3), 100)
                process_bar.setValue(process_percentage)

            score_value = self.findChild(QLabel, "performance_score_value")
            score_bar = self.findChild(QProgressBar, "performance_score_bar")
            if score_value and score_bar:
                score_value.setText(f"{self.gm_se}%")
                score_bar.setValue(self.gm_se)

            if hasattr(self, 'score_desc'):
                self.score_desc.setText(score_message)

            self.last_update_time = current_time

        except Exception as e:
            print(f"Error updating metrics: {e}")
