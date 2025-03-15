import os
import logging
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QCheckBox, 
    QGroupBox, QGridLayout, QLabel
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

from frontend.ui.gl_st import GS

class SY(QScrollArea):
    
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("SecurityTab")
        self.init_ui()
        
    def init_ui(self):
        self.setWidgetResizable(True)
        self.setFrameShape(QScrollArea.NoFrame)
        
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(10, 15, 10, 15)
        layout.setSpacing(20)  

        system_group = QGroupBox("System Security")
        system_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        system_layout = QGridLayout()
        system_layout.setContentsMargins(15, 20, 15, 20)  
        system_layout.setHorizontalSpacing(30)  
        system_layout.setVerticalSpacing(15)    
        system_layout.setColumnStretch(0, 1)
        system_layout.setColumnStretch(1, 1)

        tweaks = [
            ("restrict_anonymous_access", "Restrict Anonymous Access", 
             "Restricts anonymous access to system resources"),
            
            ("disable_smb1", "Disable SMBv1 Protocol", 
             "Disables the vulnerable SMBv1 protocol"),
            
            ("enable_uac", "Enable User Account Control", 
             "Enables UAC for better security"),
            
            ("enable_secure_boot", "Enable Secure Boot", 
             "Enables secure boot to prevent unauthorized OS loading"),
            
            ("disable_remote_assistance", "Disable Remote Assistance", 
             "Disables Windows Remote Assistance"),
            
            ("disable_autorun", "Disable AutoRun", 
             "Disables AutoRun for removable media")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "security")

            GS.ay_ck(checkbox)
            
            system_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        system_group.setLayout(system_layout)
        layout.addWidget(system_group)

        features_group = QGroupBox("Windows Features")
        features_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        features_layout = QGridLayout()
        features_layout.setContentsMargins(15, 20, 15, 20)  
        features_layout.setHorizontalSpacing(30)  
        features_layout.setVerticalSpacing(15)    
        features_layout.setColumnStretch(0, 1)
        features_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_windows_defender", "Disable Windows Defender", 
             "Disables Windows Defender (use only if you have alternative protection)"),
            
            ("disable_windows_updates", "Disable Windows Updates", 
             "Disables automatic Windows updates (not recommended for security)"),
            
            ("disable_firewall", "Disable Windows Firewall", 
             "Disables Windows Firewall (use only if you have alternative protection)"),
            
            ("disable_smartscreen_filter", "Disable SmartScreen Filter", 
             "Disables SmartScreen Filter (not recommended for security)"),
            
            ("enhance_smartscreen", "Enhance SmartScreen Protection", 
             "Enhances SmartScreen protection for better security"),
            
            ("disable_web_search", "Disable Web Search in Start Menu", 
             "Disables web search results in the Start Menu")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "security")

            GS.ay_ck(checkbox)
            
            features_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        features_group.setLayout(features_layout)
        layout.addWidget(features_group)

        network_group = QGroupBox("Network Security")
        network_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        network_layout = QGridLayout()
        network_layout.setContentsMargins(15, 20, 15, 20)  
        network_layout.setHorizontalSpacing(30)  
        network_layout.setVerticalSpacing(15)    
        network_layout.setColumnStretch(0, 1)
        network_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_netbios", "Disable NetBIOS", 
             "Disables NetBIOS over TCP/IP"),
            
            ("disable_llmnr", "Disable LLMNR", 
             "Disables Link-Local Multicast Name Resolution"),
            
            ("disable_wpad", "Disable WPAD", 
             "Disables Web Proxy Auto-Discovery Protocol"),
            
            ("disable_ipv6", "Disable IPv6", 
             "Disables IPv6 protocol (use only if not needed)")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "security")

            GS.ay_ck(checkbox)
            
            network_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        network_group.setLayout(network_layout)
        layout.addWidget(network_group)

        file_group = QGroupBox("File Security")
        file_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        file_layout = QGridLayout()
        file_layout.setContentsMargins(15, 20, 15, 20)  
        file_layout.setHorizontalSpacing(30)  
        file_layout.setVerticalSpacing(15)    
        file_layout.setColumnStretch(0, 1)
        file_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_preview_handlers", "Disable Preview Handlers", 
             "Disables file preview handlers that could be exploited"),
            
            ("disable_handle_history", "Disable Handle History", 
             "Disables tracking of file handles"),
            
            ("disable_metadata_retrieval", "Disable Metadata Retrieval", 
             "Disables automatic retrieval of file metadata"),
            
            ("disable_thumbnails", "Disable Thumbnails", 
             "Disables generation of file thumbnails")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "security")

            GS.ay_ck(checkbox)
            
            file_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        file_group.setLayout(file_layout)
        layout.addWidget(file_group)

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
        
        system_group.setStyleSheet(group_style)
        features_group.setStyleSheet(group_style)
        network_group.setStyleSheet(group_style)
        file_group.setStyleSheet(group_style)
        
        layout.addStretch()
        self.setWidget(content) 