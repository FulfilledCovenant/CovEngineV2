import os
import logging
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QCheckBox, 
    QGroupBox, QGridLayout, QLabel
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

from frontend.ui.gl_st import GS

class PY(QScrollArea):
    
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("PrivacyTab")
        self.init_ui()
        
    def init_ui(self):
        self.setWidgetResizable(True)
        self.setFrameShape(QScrollArea.NoFrame)
        
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(10, 15, 10, 15)
        layout.setSpacing(20)  

        telemetry_group = QGroupBox("Telemetry & Diagnostics")
        telemetry_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        telemetry_layout = QGridLayout()
        telemetry_layout.setContentsMargins(15, 20, 15, 20)  
        telemetry_layout.setHorizontalSpacing(30)  
        telemetry_layout.setVerticalSpacing(15)    
        telemetry_layout.setColumnStretch(0, 1)
        telemetry_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_telemetry", "Disable Telemetry", 
             "Disables Windows telemetry data collection"),
            
            ("disable_diagnostic_data", "Disable Diagnostic Data", 
             "Disables diagnostic data collection"),
            
            ("disable_feedback", "Disable Feedback", 
             "Disables Windows feedback requests"),
            
            ("disable_tailored_experiences", "Disable Tailored Experiences", 
             "Disables personalized content based on diagnostic data")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "privacy")

            GS.ay_ck(checkbox)
            
            telemetry_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        telemetry_group.setLayout(telemetry_layout)
        layout.addWidget(telemetry_group)

        location_group = QGroupBox("Location & Activity")
        location_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        location_layout = QGridLayout()
        location_layout.setContentsMargins(15, 20, 15, 20)  
        location_layout.setHorizontalSpacing(30)  
        location_layout.setVerticalSpacing(15)    
        location_layout.setColumnStretch(0, 1)
        location_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_location_tracking", "Disable Location Tracking", 
             "Disables location tracking for all apps"),
            
            ("disable_activity_history", "Disable Activity History", 
             "Disables collection of activity history"),
            
            ("disable_settings_sync", "Disable Settings Sync", 
             "Disables syncing of settings to Microsoft account"),
            
            ("disable_advertising_id", "Disable Advertising ID", 
             "Disables your unique advertising ID")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "privacy")

            GS.ay_ck(checkbox)
            
            location_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        location_group.setLayout(location_layout)
        layout.addWidget(location_group)

        permissions_group = QGroupBox("App Permissions")
        permissions_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        permissions_layout = QGridLayout()
        permissions_layout.setContentsMargins(15, 20, 15, 20)  
        permissions_layout.setHorizontalSpacing(30)  
        permissions_layout.setVerticalSpacing(15)    
        permissions_layout.setColumnStretch(0, 1)
        permissions_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_app_access_to_location", "Disable App Access to Location", 
             "Prevents apps from accessing your location"),
            
            ("disable_app_access_to_account_info", "Disable App Access to Account Info", 
             "Prevents apps from accessing your account information"),
            
            ("disable_app_access_to_contacts", "Disable App Access to Contacts", 
             "Prevents apps from accessing your contacts"),
            
            ("disable_app_access_to_calendar", "Disable App Access to Calendar", 
             "Prevents apps from accessing your calendar"),
            
            ("disable_app_access_to_call_history", "Disable App Access to Call History", 
             "Prevents apps from accessing your call history"),
            
            ("disable_app_access_to_email", "Disable App Access to Email", 
             "Prevents apps from accessing your email"),
            
            ("disable_app_access_to_messages", "Disable App Access to Messages", 
             "Prevents apps from accessing your messages"),
            
            ("disable_app_access_to_phone", "Disable App Access to Phone", 
             "Prevents apps from accessing your phone")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "privacy")

            GS.ay_ck(checkbox)
            
            permissions_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        permissions_group.setLayout(permissions_layout)
        layout.addWidget(permissions_group)

        media_group = QGroupBox("Media & Files")
        media_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        media_layout = QGridLayout()
        media_layout.setContentsMargins(15, 20, 15, 20)  
        media_layout.setHorizontalSpacing(30)  
        media_layout.setVerticalSpacing(15)    
        media_layout.setColumnStretch(0, 1)
        media_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_app_access_to_documents", "Disable App Access to Documents", 
             "Prevents apps from accessing your documents"),
            
            ("disable_app_access_to_pictures", "Disable App Access to Pictures", 
             "Prevents apps from accessing your pictures"),
            
            ("disable_app_access_to_videos", "Disable App Access to Videos", 
             "Prevents apps from accessing your videos"),
            
            ("disable_app_access_to_other_devices", "Disable App Access to Other Devices", 
             "Prevents apps from accessing other devices")
        ]
        
        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "privacy")

            GS.ay_ck(checkbox)
            
            media_layout.addWidget(checkbox, row, col)
            
            col = 1 - col  
            if col == 0:
                row += 1
                
        media_group.setLayout(media_layout)
        layout.addWidget(media_group)

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
        
        telemetry_group.setStyleSheet(group_style)
        location_group.setStyleSheet(group_style)
        permissions_group.setStyleSheet(group_style)
        media_group.setStyleSheet(group_style)
        
        layout.addStretch()
        self.setWidget(content) 