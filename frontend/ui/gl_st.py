from PyQt5.QtWidgets import QGraphicsOpacityEffect, QWidget
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QTimer, Qt, QSize, QRect
from PyQt5.QtGui import QColor, QPainter, QLinearGradient, QPainterPath, QPen, QBrush

class GS:

    DARK_THEME = {
        "bg_primary": "#121212",
        "bg_secondary": "#1e1e1e",
        "bg_tertiary": "#2a2a2a",
        "bg_hover": "#383838",
        "bg_active": "#404040",
        "accent": "#3d5afe",
        "accent_hover": "#536dfe",
        "accent_active": "#2a3eb1",
        "text_primary": "#ffffff",
        "text_secondary": "#b0b0b0",
        "text_on_accent": "#ffffff",
        "success": "#4CAF50",
        "warning": "#FF9800",
        "error": "#F44336",
        "info": "#2196F3"
    }

    @staticmethod
    def ay_ts(widget):
        """)

    @staticmethod
    def ay_gs(widget):
        """)

    @staticmethod
    def ay_bn(widget):
        """)

    @staticmethod
    def apply_button_style(widget, secondary=False):
        if not secondary:
            """)
        else:
            """)

    @staticmethod
    def ay_ck(widget):
        """)

    @staticmethod
    def ay_fd(widget, duration=300):
        if not widget:
            return None

        opacity_effect = QGraphicsOpacityEffect(widget)
        opacity_effect.setOpacity(0)
        widget.setGraphicsEffect(opacity_effect)

        fade_anim = QPropertyAnimation(opacity_effect, b"opacity")
        fade_anim.setDuration(duration)
        fade_anim.setStartValue(0)
        fade_anim.setEndValue(1)
        fade_anim.setEasingCurve(QEasingCurve.OutCubic)
        fade_anim.start()

        return fade_anim

    @staticmethod
    def ay_sl(widget, direction="right", distance=50, duration=300):
        original_pos = widget.pos()

        if direction == "right":
            widget.move(original_pos.x() - distance, original_pos.y())
        elif direction == "left":
            widget.move(original_pos.x() + distance, original_pos.y())
        elif direction == "up":
            widget.move(original_pos.x(), original_pos.y() + distance)
        elif direction == "down":
            widget.move(original_pos.x(), original_pos.y() - distance)

        slide_anim = QPropertyAnimation(widget, b"pos")
        slide_anim.setDuration(duration)
        slide_anim.setEndValue(original_pos)
        slide_anim.setEasingCurve(QEasingCurve.OutCubic)
        slide_anim.start()

        return slide_anim

class GW(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setStyleSheet(f"background-color: {GS.DARK_THEME['bg_secondary']}")
        self.is_painting = False

    def paintEvent(self, event):
        super().paintEvent(event)

        if self.is_painting:
            return

        self.is_painting = True

        try:
            painter = QPainter()
            if painter.begin(self):
                painter.setRenderHint(QPainter.Antialiasing)

                path = QPainterPath()
                rect = self.rect()
                path.addRoundedRect(rect.x(), rect.y(), rect.width(), rect.height(), 10, 10)

                gradient = QLinearGradient(0, 0, 0, self.height())
                gradient.setColorAt(0, QColor(60, 60, 60, 230))
                gradient.setColorAt(0.5, QColor(40, 40, 40, 230))
                gradient.setColorAt(1, QColor(30, 30, 30, 230))

                painter.fillPath(path, gradient)

                highlight_path = QPainterPath()
                highlight_rect = self.rect()
                highlight_height = int(self.height() * 0.4)
                highlight_rect.setHeight(highlight_height)

                highlight_path.addRoundedRect(highlight_rect.x(), highlight_rect.y(),
                                            highlight_rect.width(), highlight_rect.height(), 10, 10)

                highlight_gradient = QLinearGradient(0, 0, 0, highlight_rect.height())
                highlight_gradient.setColorAt(0, QColor(255, 255, 255, 40))
                highlight_gradient.setColorAt(1, QColor(255, 255, 255, 0))

                painter.fillPath(highlight_path, highlight_gradient)

                painter.setPen(QPen(QColor(255, 255, 255, 30), 1))
                painter.drawPath(path)

                painter.end()
        except Exception as e:
            print(f"Error painting glossy widget: {e}")
        finally:
            self.is_painting = False
