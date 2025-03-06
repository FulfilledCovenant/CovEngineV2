from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QSizePolicy)
from PyQt5.QtCore import Qt, QTimer, QRectF, QPointF, QSize
from PyQt5.QtGui import QPainter, QPainterPath, QColor, QPen, QBrush, QLinearGradient, QFont

import psutil
import time
import math
from collections import deque

class LC(QWidget):
    def __init__(self, title="", max_points=60, parent=None):
        super().__init__(parent)
        self.title = title
        self.data_points = deque(maxlen=max_points)
        self.max_value = 100
        self.min_value = 0
        self.color = QColor("#3d5afe")
        self.gradient_top = QColor("#3d5afe")
        self.gradient_bottom = QColor(61, 90, 254, 40)

        for _ in range(max_points):
            self.data_points.append(0)

        self.setMinimumSize(200, 150)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def ad_pt(self, value):
        self.data_points.append(value)

        if value > self.max_value * 0.9:
            self.max_value = value * 1.1

        self.update()

    def st_cl(self, color, gradient_top=None, gradient_bottom=None):
        self.color = QColor(color)

        if gradient_top:
            self.gradient_top = QColor(gradient_top)
        else:
            self.gradient_top = self.color

        if gradient_bottom:
            self.gradient_bottom = QColor(gradient_bottom)
        else:
            self.gradient_bottom = QColor(self.color)
            self.gradient_bottom.setAlpha(40)

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.title:
            painter.setPen(Qt.white)
            title_font = QFont()
            title_font.setBold(True)
            painter.setFont(title_font)
            painter.drawText(10, 20, self.title)

        chart_rect = QRectF(10, 30, self.width() - 20, self.height() - 40)

        bg_path = QPainterPath()
        bg_path.addRoundedRect(chart_rect, 5, 5)
        painter.fillPath(bg_path, QBrush(QColor(30, 30, 30, 100)))

        painter.setPen(QPen(QColor(255, 255, 255, 30), 1, Qt.DashLine))

        for i in range(1, 4):
            y = chart_rect.top() + (chart_rect.height() * (i / 4))
            painter.drawLine(QPointF(chart_rect.left(), y), QPointF(chart_rect.right(), y))

            painter.setPen(Qt.white)
            percent = 100 - (i * 25)
            painter.drawText(QPointF(chart_rect.left() - 5, y + 5), f"{percent}%")

        points_count = len(self.data_points)
        if points_count > 10:
            step = max(1, points_count // 6)
            for i in range(0, points_count, step):
                x = chart_rect.left() + (chart_rect.width() * (1 - (i / points_count)))
                painter.setPen(QPen(QColor(255, 255, 255, 30), 1, Qt.DashLine))
                painter.drawLine(QPointF(x, chart_rect.top()), QPointF(x, chart_rect.bottom()))

        if not self.data_points or all(x == 0 for x in self.data_points):
            return

        path = QPainterPath()

        fill_path = QPainterPath()

        point_width = chart_rect.width() / (len(self.data_points) - 1) if len(self.data_points) > 1 else 0

        fill_path.moveTo(chart_rect.left(), chart_rect.bottom())

        first_y = chart_rect.bottom() - (self.data_points[0] / self.max_value) * chart_rect.height()
        path.moveTo(chart_rect.left(), first_y)
        fill_path.lineTo(chart_rect.left(), first_y)

        for i in range(1, len(self.data_points)):
            x = chart_rect.left() + i * point_width
            y = chart_rect.bottom() - (self.data_points[i] / self.max_value) * chart_rect.height()

            path.lineTo(x, y)

            fill_path.lineTo(x, y)

        fill_path.lineTo(chart_rect.right(), chart_rect.bottom())
        fill_path.closeSubpath()

        gradient = QLinearGradient(0, chart_rect.top(), 0, chart_rect.bottom())
        gradient.setColorAt(0, self.gradient_top)
        gradient.setColorAt(1, self.gradient_bottom)
        painter.fillPath(fill_path, gradient)

        painter.setPen(QPen(self.color, 2))
        painter.drawPath(path)

        current_value = self.data_points[-1] if self.data_points else 0
        value_text = f"{current_value:.1f}"
        painter.setPen(Qt.white)
        value_font = QFont()
        value_font.setBold(True)
        value_font.setPointSize(12)
        painter.setFont(value_font)
        painter.drawText(chart_rect.right() - 50, 20, value_text)

class GG(QWidget):
    def __init__(self, title="", parent=None):
        super().__init__(parent)
        self.title = title
        self.value = 0
        self.min_value = 0
        self.max_value = 100
        self.color = QColor("#3d5afe")
        self.warning_threshold = 70
        self.critical_threshold = 90
        self.warning_color = QColor("#FF9800")
        self.critical_color = QColor("#F44336")

        self.setMinimumSize(150, 150)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def st_ve(self, value):
        self.value = max(self.min_value, min(value, self.max_value))
        self.update()

    def st_rs(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.update()

    def st_ts(self, warning, critical):
        self.warning_threshold = warning
        self.critical_threshold = critical
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        center = QPointF(self.width() / 2, self.height() / 2 + 10)
        outer_radius = min(self.width(), self.height()) / 2 - 10
        inner_radius = outer_radius * 0.7

        if self.title:
            painter.setPen(Qt.white)
            title_font = QFont()
            title_font.setBold(True)
            painter.setFont(title_font)
            text_rect = QRectF(0, 5, self.width(), 20)
            painter.drawText(text_rect, Qt.AlignCenter, self.title)

        painter.setPen(QPen(QColor(60, 60, 60), 10, Qt.SolidLine, Qt.RoundCap))
        painter.drawArc(center.x() - outer_radius, center.y() - outer_radius,
                       outer_radius * 2, outer_radius * 2,
                       225 * 16, 90 * 16)

        value_range = self.max_value - self.min_value
        value_angle = 90 * (self.value - self.min_value) / value_range

        if self.value >= self.critical_threshold:
            arc_color = self.critical_color
        elif self.value >= self.warning_threshold:
            arc_color = self.warning_color
        else:
            arc_color = self.color

        painter.setPen(QPen(arc_color, 10, Qt.SolidLine, Qt.RoundCap))
        painter.drawArc(center.x() - outer_radius, center.y() - outer_radius,
                       outer_radius * 2, outer_radius * 2,
                       225 * 16, -value_angle * 16)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(30, 30, 30))
        painter.drawEllipse(center, inner_radius, inner_radius)

        painter.setPen(Qt.white)
        value_font = QFont()
        value_font.setBold(True)
        value_font.setPointSize(16)
        painter.setFont(value_font)

        value_text = f"{int(self.value)}"
        text_rect = QRectF(center.x() - inner_radius, center.y() - inner_radius / 2,
                          inner_radius * 2, inner_radius)
        painter.drawText(text_rect, Qt.AlignCenter, value_text)

        percent_font = QFont()
        percent_font.setPointSize(10)
        painter.setFont(percent_font)
        percent_rect = QRectF(center.x() - inner_radius, center.y() + 5,
                             inner_radius * 2, inner_radius / 2)
        painter.drawText(percent_rect, Qt.AlignCenter, "%")

class CM(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.cpu_chart = LC("CPU Usage (%)", max_points=60)
        self.cpu_chart.st_cl("#3d5afe")
        layout.addWidget(self.cpu_chart)

        self.core_gauges = []

        self.cpu_count = min(4, psutil.cpu_count(logical=True))

        for i in range(self.cpu_count):
            gauge = GG(f"Core {i+1}")
            self.layout().addWidget(gauge)
            self.core_gauges.append(gauge)

        self.last_update_time = 0
        self.ud_dt()

    def ud_dt(self):
        current_time = time.time()
        if current_time - self.last_update_time < 1.0:
            return

        try:
            cpu_percent = psutil.cpu_percent(interval=None)
            self.cpu_chart.ad_pt(cpu_percent)

            per_cpu = psutil.cpu_percent(interval=None, percpu=True)

            for i in range(min(len(per_cpu), len(self.core_gauges))):
                self.core_gauges[i].st_ve(per_cpu[i])

            self.last_update_time = current_time
        except Exception as e:
            print(f"Error updating CPU data: {e}")

class MM(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.memory_chart = LC("Memory Usage (%)", max_points=60)
        self.memory_chart.st_cl("#4CAF50", "#4CAF50", QColor(76, 175, 80, 40))
        layout.addWidget(self.memory_chart)

        self.memory_gauge = GG("RAM")
        layout.addWidget(self.memory_gauge)

        swap = psutil.swap_memory()
        if swap.total > 0:
            self.swap_gauge = GG("Swap")
            layout.addWidget(self.swap_gauge)
        else:
            self.swap_gauge = None

        self.last_update_time = 0
        self.ud_dt()

    def ud_dt(self):
        current_time = time.time()
        if current_time - self.last_update_time < 1.0:
            return

        try:
            memory = psutil.virtual_memory()
            self.memory_chart.ad_pt(memory.percent)
            self.memory_gauge.st_ve(memory.percent)

            if self.swap_gauge:
                swap = psutil.swap_memory()
                self.swap_gauge.st_ve(swap.percent)

            self.last_update_time = current_time
        except Exception as e:
            print(f"Error updating memory data: {e}")

class NM(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.download_chart = LC("Download (KB/s)", max_points=60)
        self.download_chart.st_cl("#2196F3")
        layout.addWidget(self.download_chart)

        self.upload_chart = LC("Upload (KB/s)", max_points=60)
        self.upload_chart.st_cl("#F44336")
        layout.addWidget(self.upload_chart)

        self.last_net_io = psutil.net_io_counters()
        self.last_time = time.time()
        self.last_update_time = 0

    def ud_dt(self):
        current_time = time.time()
        if current_time - self.last_update_time < 1.0:
            return

        try:
            current_net_io = psutil.net_io_counters()

            time_diff = current_time - self.last_time

            if time_diff > 0:
                download_speed = (current_net_io.bytes_recv - self.last_net_io.bytes_recv) / 1024 / time_diff
                upload_speed = (current_net_io.bytes_sent - self.last_net_io.bytes_sent) / 1024 / time_diff

                self.download_chart.ad_pt(download_speed)
                self.upload_chart.ad_pt(upload_speed)

                self.last_net_io = current_net_io
                self.last_time = current_time

            self.last_update_time = current_time
        except Exception as e:
            print(f"Error updating network data: {e}")
