import os
import logging
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QCheckBox,
    QGroupBox, QGridLayout, QLabel
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

from frontend.ui.gl_st import GS

class PE(QScrollArea):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("PerformanceTab")
        self.init_ui()

    def init_ui(self):
        self.setWidgetResizable(True)
        self.setFrameShape(QScrollArea.NoFrame)

        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(10, 15, 10, 15)
        layout.setSpacing(20)

        system_group = QGroupBox("System Performance")
        system_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        system_layout = QGridLayout()
        system_layout.setContentsMargins(15, 20, 15, 20)
        system_layout.setHorizontalSpacing(30)
        system_layout.setVerticalSpacing(15)
        system_layout.setColumnStretch(0, 1)
        system_layout.setColumnStretch(1, 1)

        tweaks = [
            ("configure_bcdedit", "Configure BCDEdit",
             "Optimizes boot configuration data for performance"),

            ("disable_background_apps", "Disable Background Apps",
             "Prevents apps from running in the background"),

            ("disable_memory_compression", "Disable Memory Compression",
             "Disables Windows memory compression feature"),

            ("set_ram_usage_high", "Set RAM Usage High",
             "Configures Windows to prioritize performance over memory usage")
        ]

        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "performance")
            GS.ay_ck(checkbox)

            system_layout.addWidget(checkbox, row, col)

            col = 1 - col
            if col == 0:
                row += 1

        system_group.setLayout(system_layout)
        layout.addWidget(system_group)

        memory_group = QGroupBox("Memory Management")
        memory_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        memory_layout = QGridLayout()
        memory_layout.setContentsMargins(15, 20, 15, 20)
        memory_layout.setHorizontalSpacing(30)
        memory_layout.setVerticalSpacing(15)
        memory_layout.setColumnStretch(0, 1)
        memory_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_pagefile", "Disable PageFile",
             "Disables the Windows page file (virtual memory)"),

            ("configure_mmcss", "Configure MMCSS",
             "Optimizes Multimedia Class Scheduler Service"),

            ("disable_paging_settings", "Disable Paging Settings",
             "Adjusts paging settings for better performance"),

            ("disable_prefetch", "Disable Prefetch",
             "Disables Windows prefetch feature")
        ]

        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "performance")
            GS.ay_ck(checkbox)

            memory_layout.addWidget(checkbox, row, col)

            col = 1 - col
            if col == 0:
                row += 1

        memory_group.setLayout(memory_layout)
        layout.addWidget(memory_group)

        services_group = QGroupBox("System Services")
        services_group.setFont(QFont("Segoe UI", 10, QFont.Bold))
        services_layout = QGridLayout()
        services_layout.setContentsMargins(15, 20, 15, 20)
        services_layout.setHorizontalSpacing(30)
        services_layout.setVerticalSpacing(15)
        services_layout.setColumnStretch(0, 1)
        services_layout.setColumnStretch(1, 1)

        tweaks = [
            ("disable_automatic_folder_discovery", "Disable Automatic Folder Discovery",
             "Disables automatic folder type discovery"),

            ("disable_boot_tracing", "Disable Boot Tracing",
             "Disables boot tracing for faster startup"),

            ("disable_fault_tolerant_heap", "Disable Fault Tolerant Heap",
             "Disables fault tolerant heap for better performance"),

            ("disable_service_host_splitting", "Disable Service Host Splitting",
             "Combines service hosts for reduced memory usage"),

            ("disable_sleep_study", "Disable Sleep Study",
             "Disables Windows sleep study feature"),

            ("disable_spectre_and_meltdown", "Disable Spectre and Meltdown Protection",
             "Disables CPU vulnerability protections for better performance")
        ]

        row = 0
        col = 0
        for tweak_id, tweak_name, tweak_desc in tweaks:
            checkbox = QCheckBox(tweak_name)
            checkbox.setFont(QFont("Segoe UI", 10))
            checkbox.setToolTip(tweak_desc)
            checkbox.setProperty("tweak_id", tweak_id)
            checkbox.setProperty("category", "performance")
            GS.ay_ck(checkbox)

            services_layout.addWidget(checkbox, row, col)

            col = 1 - col
            if col == 0:
                row += 1

        services_group.setLayout(services_layout)
        layout.addWidget(services_group)


        system_group.setStyleSheet(group_style)
        memory_group.setStyleSheet(group_style)
        services_group.setStyleSheet(group_style)

        layout.addStretch()
        self.setWidget(content)
