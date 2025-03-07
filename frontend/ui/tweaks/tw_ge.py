import os
import logging
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QCheckBox, 
    QGroupBox, QGridLayout, QLabel
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

from frontend.ui.gl_st import GS

class GE(QScrollArea):
    
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("GamingTab")
        self.init_ui()
        
    def init_ui(self):
        self.setWidgetResizable(True)
        self.setFrameShape(QScrollArea.NoFrame)
        
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(10, 15, 10, 15)
        layout.setSpacing(20)  

        input_group = QGroupBox("Input & Response")
        input_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        input_layout = QGridLayout()
        input_layout.setContentsMargins(15, 20, 15, 20)  
        input_layout.setHorizontalSpacing(30)  
        input_layout.setVerticalSpacing(15)    
        input_layout.setColumnStretch(0, 1)
        input_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_mouse_acceleration", "Disable Mouse Acceleration", 
             "Disables mouse acceleration for more precise aiming"),
            
            ("optimize_mouse_settings", "Optimize Mouse Settings", 
             "Adjusts mouse settings for gaming"),
            
            ("reduce_input_delay", "Reduce Input Delay", 
             "Minimizes input lag for faster response times"),
            
            ("optimize_keyboard_settings", "Optimize Keyboard Settings", 
             "Adjusts keyboard settings for gaming")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "gaming")

            GS.ay_ck(checkbox)
            
            input_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)

        features_group = QGroupBox("Game Features")
        features_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        features_layout = QGridLayout()
        features_layout.setContentsMargins(15, 20, 15, 20)  
        features_layout.setHorizontalSpacing(30)  
        features_layout.setVerticalSpacing(15)    
        features_layout.setColumnStretch(0, 1)
        features_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_game_bar", "Disable Game Bar", 
             "Disables the Windows Game Bar to free up resources"),
            
            ("disable_game_dvr", "Disable Game DVR", 
             "Disables background recording of gameplay"),
            
            ("enable_game_mode", "Enable Game Mode", 
             "Enables Windows Game Mode for better performance"),
            
            ("optimize_fullscreen", "Optimize Fullscreen Mode", 
             "Ensures games run in true fullscreen mode"),
            
            ("disable_nagle_algorithm", "Disable Nagle's Algorithm", 
             "Reduces network latency for online games"),
            
            ("optimize_network_settings", "Optimize Network Settings", 
             "Adjusts network settings for online gaming")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "gaming")

            GS.ay_ck(checkbox)
            
            features_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        features_group.setLayout(features_layout)
        layout.addWidget(features_group)

        power_group = QGroupBox("Power & Performance")
        power_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        power_layout = QGridLayout()
        power_layout.setContentsMargins(15, 20, 15, 20)  
        power_layout.setHorizontalSpacing(30)  
        power_layout.setVerticalSpacing(15)    
        power_layout.setColumnStretch(0, 1)
        power_layout.setColumnStretch(1, 1)

        tweaks = [
            ("ultimate_performance", "Enable Ultimate Performance Power Plan", 
             "Activates the hidden Ultimate Performance power plan"),
            
            ("disable_power_throttling", "Disable Power Throttling", 
             "Prevents CPU throttling to maintain maximum performance"),
            
            ("optimize_power_options", "Optimize Power Options", 
             "Adjusts power settings for gaming performance"),
            
            ("disable_core_parking", "Disable Core Parking", 
             "Prevents Windows from parking CPU cores to save power")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "gaming")

            GS.ay_ck(checkbox)
            
            power_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        power_group.setLayout(power_layout)
        layout.addWidget(power_group)

        graphics_group = QGroupBox("Graphics & Display")
        graphics_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        graphics_layout = QGridLayout()
        graphics_layout.setContentsMargins(15, 20, 15, 20)  
        graphics_layout.setHorizontalSpacing(30)  
        graphics_layout.setVerticalSpacing(15)    
        graphics_layout.setColumnStretch(0, 1)
        graphics_layout.setColumnStretch(1, 1)

        tweaks = [
            ("optimize_gpu_settings", "Optimize GPU Settings", 
             "Adjusts GPU settings for gaming performance"),
            
            ("disable_vsync", "Disable VSync", 
             "Disables vertical synchronization for higher FPS"),
            
            ("optimize_display_scaling", "Optimize Display Scaling", 
             "Adjusts display scaling for better performance"),
            
            ("disable_fullscreen_optimizations", "Disable Fullscreen Optimizations", 
             "Disables Windows fullscreen optimizations that can cause issues")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "gaming")

            GS.ay_ck(checkbox)
            
            graphics_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        graphics_group.setLayout(graphics_layout)
        layout.addWidget(graphics_group)

        group_style = f"""
            QGroupBox {{
                border: 1px solid {GS.DARK_THEME['bg_tertiary']};
                border-radius: 8px;
                margin-top: 16px;
                background-color: {GS.DARK_THEME['bg_secondary']};
            }}
            
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
                color: {GS.DARK_THEME['text_primary']};
            }}
        """
        
        input_group.setStyleSheet(group_style)
        features_group.setStyleSheet(group_style)
        power_group.setStyleSheet(group_style)
        graphics_group.setStyleSheet(group_style)
        
        layout.addStretch()
        self.setWidget(content) 