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
             "Adjusts keyboard settings for gaming"),
             
            ("optimize_controller_settings", "Optimize Controller Settings", 
             "Adjusts controller settings for better gaming experience"),
             
            ("enhance_pointer_precision", "Enhance Pointer Precision", 
             "Improves mouse precision for better aiming in games")
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
        
        graphics_group = QGroupBox("Graphics & Performance")
        graphics_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        graphics_layout = QGridLayout()
        graphics_layout.setContentsMargins(15, 20, 15, 20)
        graphics_layout.setHorizontalSpacing(30)
        graphics_layout.setVerticalSpacing(15)
        graphics_layout.setColumnStretch(0, 1)
        graphics_layout.setColumnStretch(1, 1)
        
        tweaks = [
            ("disable_game_bar", "Disable Game Bar", 
             "Disables Windows Game Bar for better performance"),
            
            ("disable_game_dvr", "Disable Game DVR", 
             "Disables Game DVR recording functionality"),
            
            ("enable_game_mode", "Enable Game Mode", 
             "Enables Windows Game Mode for better performance"),
            
            ("disable_fullscreen_optimizations", "Disable Fullscreen Optimizations", 
             "Disables Windows fullscreen optimizations"),
             
            ("optimize_gpu_settings", "Optimize GPU Settings", 
             "Adjusts GPU settings for better gaming performance"),
             
            ("optimize_directx", "Optimize DirectX", 
             "Optimizes DirectX settings for better gaming performance"),
             
            ("optimize_vulkan", "Optimize Vulkan", 
             "Optimizes Vulkan settings for better gaming performance")
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
        
        network_group = QGroupBox("Network Optimization")
        network_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        network_layout = QGridLayout()
        network_layout.setContentsMargins(15, 20, 15, 20)
        network_layout.setHorizontalSpacing(30)
        network_layout.setVerticalSpacing(15)
        network_layout.setColumnStretch(0, 1)
        network_layout.setColumnStretch(1, 1)
        
        tweaks = [
            ("optimize_tcp_settings", "Optimize TCP Settings", 
             "Optimizes TCP settings for better network performance"),
            
            ("optimize_udp_settings", "Optimize UDP Settings", 
             "Optimizes UDP settings for better network performance"),
            
            ("reduce_network_latency", "Reduce Network Latency", 
             "Adjusts settings to reduce network latency"),
            
            ("prioritize_game_traffic", "Prioritize Game Traffic", 
             "Prioritizes game network traffic for better performance"),
             
            ("optimize_dns_settings", "Optimize DNS Settings", 
             "Configures DNS settings for faster response times")
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
            
            network_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
        
        network_group.setLayout(network_layout)
        layout.addWidget(network_group)
        
        advanced_group = QGroupBox("Advanced Tweaks")
        advanced_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        advanced_layout = QGridLayout()
        advanced_layout.setContentsMargins(15, 20, 15, 20)
        advanced_layout.setHorizontalSpacing(30)
        advanced_layout.setVerticalSpacing(15)
        advanced_layout.setColumnStretch(0, 1)
        advanced_layout.setColumnStretch(1, 1)
        
        tweaks = [
            ("disable_hpet", "Disable HPET", 
             "Disables High Precision Event Timer for reduced latency"),
            
            ("disable_onedrive", "Disable OneDrive", 
             "Disables Microsoft OneDrive to free up resources"),
            
            ("disable_superfetch", "Disable SuperFetch", 
             "Disables SuperFetch/SysMain service for better gaming performance"),
            
            ("disable_hibernation", "Disable Hibernation", 
             "Disables system hibernation to free up disk space"),
             
            ("optimize_timer_resolution", "Optimize Timer Resolution", 
             "Sets Windows timer resolution to 0.5ms for smoother gameplay"),
             
            ("disable_dynamic_tick", "Disable Dynamic Tick", 
             "Disables dynamic tick for more consistent performance"),
             
            ("disable_nvidia_telemetry", "Disable NVIDIA Telemetry", 
             "Disables NVIDIA telemetry services"),
             
            ("disable_amd_telemetry", "Disable AMD Telemetry", 
             "Disables AMD telemetry services")
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
            
            advanced_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
        
        advanced_group.setLayout(advanced_layout)
        layout.addWidget(advanced_group)
        
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
        graphics_group.setStyleSheet(group_style)
        network_group.setStyleSheet(group_style)
        advanced_group.setStyleSheet(group_style)
        
        layout.addStretch()
        
        self.setWidget(content) 