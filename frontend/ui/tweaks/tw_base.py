from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                               QCheckBox, QScrollArea, QFrame, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from frontend.ui.gl_st import GS  

class BS(QWidget):
    def __init__(self):
        super().__init__()
        self.checkbox_map = {}  
        self.setup_ui()
        
    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setStyleSheet("background: transparent; border: none;")
        
        tweaks_container = QWidget()
        tweaks_container.setStyleSheet("background: transparent;")
        self.tweaks_layout = QVBoxLayout(tweaks_container)
        self.tweaks_layout.setContentsMargins(0, 0, 0, 0)
        self.tweaks_layout.setSpacing(15)
        
        scroll_area.setWidget(tweaks_container)
        main_layout.addWidget(scroll_area)
    
    def add_tweak(self, tweak_id, name, description, default_value="YES", safety="Safe"):
        tweak_frame = QFrame()
        tweak_frame.setFrameShape(QFrame.StyledPanel)
        tweak_frame.setStyleSheet(f"""
            QFrame {{ 
                background-color: {GS.DARK_THEME['bg_tertiary']}; 
                border-radius: 8px; 
                margin: 5px;
                border: 1px solid rgba(255, 255, 255, 0.05);
            }}
        """)
        
        layout = QGridLayout(tweak_frame)
        layout.setContentsMargins(15, 15, 15, 15)

        checkbox = QCheckBox(name)
        checkbox_font = QFont()
        checkbox_font.setBold(True)
        checkbox.setFont(checkbox_font)
        checkbox.setStyleSheet(f"""
            QCheckBox {{
                color: {GS.DARK_THEME['text_primary']};
                spacing: 8px;
            }}
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                border: 1px solid {GS.DARK_THEME['accent']};
            }}
            QCheckBox::indicator:unchecked {{
                background-color: {GS.DARK_THEME['bg_primary']};
            }}
            QCheckBox::indicator:checked {{
                background-color: {GS.DARK_THEME['accent']};
                image: url(check.png);
            }}
        """)

        checkbox.setChecked(False)

        self.checkbox_map[tweak_id] = checkbox

        desc_label = QLabel(description)
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']}; background: transparent;")

        safety_label = QLabel(f"Safety: {safety}")

        if safety == "Safe":
            safety_color = GS.DARK_THEME["success"]  
        elif safety == "Moderate":
            safety_color = GS.DARK_THEME["warning"]  
        else:  
            safety_color = GS.DARK_THEME["error"]  
            
        safety_label.setStyleSheet(f"color: {safety_color}; font-weight: bold; background: transparent;")

        layout.addWidget(checkbox, 0, 0)
        layout.addWidget(safety_label, 0, 1, Qt.AlignRight)
        layout.addWidget(desc_label, 1, 0, 1, 2)

        self.tweaks_layout.addWidget(tweak_frame)
        
        return checkbox
    
    def add_tweaks_group(self, group_name, tweaks):

        group_frame = QFrame()
        group_frame.setFrameShape(QFrame.StyledPanel)
        group_frame.setStyleSheet(f"""
            QFrame {{ 
                background-color: {GS.DARK_THEME['bg_secondary']}; 
                border-radius: 10px; 
                border: 1px solid rgba(255, 255, 255, 0.05);
            }}
        """)
        
        group_layout = QVBoxLayout(group_frame)
        group_layout.setContentsMargins(20, 20, 20, 20)
        group_layout.setSpacing(10)
        
        group_label = QLabel(group_name)
        group_font = QFont()
        group_font.setPointSize(14)
        group_font.setBold(True)
        group_label.setFont(group_font)
        group_label.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background: transparent;")
        
        group_layout.addWidget(group_label)

        for tweak in tweaks:
            self.add_tweak(
                tweak.get("id", "unknown"),
                tweak.get("name", "Unnamed Tweak"),
                tweak.get("description", "No description provided."),
                tweak.get("default", "YES"),
                tweak.get("safety", "Safe")
            )

        self.tweaks_layout.addWidget(group_frame)
        
    def get_selected_tweaks(self):
        return [tweak_id for tweak_id, checkbox in self.checkbox_map.items() if checkbox.isChecked()]
    
    def select_all(self):
        for checkbox in self.checkbox_map.values():
            checkbox.setChecked(True)
    
    def deselect_all(self):
        for checkbox in self.checkbox_map.values():
            checkbox.setChecked(False) 