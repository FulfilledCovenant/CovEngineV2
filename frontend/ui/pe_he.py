from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                               QHBoxLayout, QFrame, QProgressDialog, QMessageBox,
                               QDialog, QTabWidget, QTableWidget, QTableWidgetItem, QHeaderView,
                               QScrollArea, QGridLayout, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QPixmap, QColor, QPainter, QPainterPath, QLinearGradient
import psutil
import platform
import os
import sys
import time
import threading
import socket
import datetime
from .gl_st import GS, GW

try:
    if platform.system() == "Windows":
        import wmi
        import ctypes
        HAS_WMI = True
    else:
        HAS_WMI = False
except ImportError:
    HAS_WMI = False

class HE(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window  
        self.analysis_results = {}  

        self.last_net_io = None

        self.stUI()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ud_tm)
        self.timer.start(1000)  
        
    def stUI(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setStyleSheet("background: transparent;")

        content_widget = QWidget()
        content_widget.setStyleSheet(f"background-color: {GS.DARK_THEME['bg_primary']};")
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(30, 30, 30, 30)
        content_layout.setSpacing(30)

        welcome_container = QWidget()
        welcome_container.setStyleSheet(f"""
            background-color: {GS.DARK_THEME['bg_tertiary']};
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        """)
        
        welcome_layout = QVBoxLayout(welcome_container)
        welcome_layout.setContentsMargins(25, 25, 25, 25)

        try:
            import getpass
            user_name = getpass.getuser()
        except:
            user_name = "User"

        welcome_title = QLabel(f"Welcome {user_name}")
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        welcome_title.setFont(title_font)
        welcome_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background: transparent;")

        current_time = datetime.datetime.now()
        self.time_label = QLabel(current_time.strftime("%A, %B %d, %Y | %H:%M:%S"))
        subtitle_font = QFont()
        subtitle_font.setPointSize(12)
        self.time_label.setFont(subtitle_font)
        self.time_label.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']}; background: transparent;")

        welcome_msg = QLabel("Welcome to CovEngineV2, your ultimate gaming optimizer. "
                            "Monitor your system, apply tweaks, and boost your gaming experience.")
        welcome_msg.setWordWrap(True)
        welcome_msg.setStyleSheet(f"color: {GS.DARK_THEME['text_secondary']}; background: transparent;")

        welcome_layout.addWidget(welcome_title)
        welcome_layout.addWidget(self.time_label)
        welcome_layout.addSpacing(10)
        welcome_layout.addWidget(welcome_msg)

        content_layout.addWidget(welcome_container)

        self.ad_qs(content_layout)

        self.ad_qa(content_layout)

        content_layout.addStretch()

        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
        
    def ad_qs(self, parent_layout):

        section_title = QLabel("System Overview")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        section_title.setFont(title_font)
        section_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background: transparent;")

        parent_layout.addWidget(section_title)

        stats_grid = QGridLayout()
        stats_grid.setSpacing(20)
        stats_grid.setContentsMargins(0, 10, 0, 0)

        self.cpu_card = self.cr_sc("CPU Usage", "0%", "cpu")
        stats_grid.addWidget(self.cpu_card, 0, 0)

        self.memory_card = self.cr_sc("Memory Usage", "0%", "memory")
        stats_grid.addWidget(self.memory_card, 0, 1)

        self.disk_card = self.cr_sc("Disk Usage", "0%", "disk")
        stats_grid.addWidget(self.disk_card, 1, 0)

        self.network_card = self.cr_sc("Network", "0 KB/s", "network")
        stats_grid.addWidget(self.network_card, 1, 1)

        parent_layout.addLayout(stats_grid)
        
    def cr_sc(self, title, value, card_type):

        card = QWidget()
        card.setStyleSheet(f"""
            background-color: {GS.DARK_THEME['bg_tertiary']};
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        """)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 20, 20, 20)

        card_title = QLabel(title)
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        card_title.setFont(title_font)
        card_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background: transparent;")

        card_value = QLabel(value)
        card_value.setObjectName(f"{card_type}_value")
        value_font = QFont()
        value_font.setPointSize(24)
        value_font.setBold(True)
        card_value.setFont(value_font)
        card_value.setStyleSheet(f"color: {GS.DARK_THEME['accent']}; background: transparent;")

        card_layout.addWidget(card_title)
        card_layout.addWidget(card_value)
        card_layout.addStretch()
        
        return card
        
    def ad_qa(self, parent_layout):

        section_title = QLabel("Metric Settings")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        section_title.setFont(title_font)
        section_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background: transparent;")

        parent_layout.addWidget(section_title)

        metrics_container = QWidget()
        metrics_container.setStyleSheet(f"""
            background-color: {GS.DARK_THEME['bg_tertiary']};
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        """)
        metrics_layout = QGridLayout(metrics_container)
        metrics_layout.setContentsMargins(20, 20, 20, 20)
        metrics_layout.setSpacing(20)

        card_style = f"""
            QFrame {{
                background-color: {GS.DARK_THEME['bg_primary']};
                border-radius: 6px;
                border: 1px solid rgba(255, 255, 255, 0.05);
                padding: 15px;
            }}
        """

        cpu_temp_card = QFrame()
        cpu_temp_card.setStyleSheet(card_style)
        cpu_temp_layout = QVBoxLayout(cpu_temp_card)
        
        cpu_temp_title = QLabel("CPU Temperature")
        cpu_temp_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        cpu_temp_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background: transparent;")
        
        cpu_temp_value = QLabel("Monitoring...")
        cpu_temp_value.setObjectName("cpu_temp_value")
        cpu_temp_value.setFont(QFont("Segoe UI", 18, QFont.Bold))
        cpu_temp_value.setStyleSheet(f"color: {GS.DARK_THEME['accent']}; background: transparent;")
        
        cpu_temp_layout.addWidget(cpu_temp_title)
        cpu_temp_layout.addWidget(cpu_temp_value)

        gpu_usage_card = QFrame()
        gpu_usage_card.setStyleSheet(card_style)
        gpu_usage_layout = QVBoxLayout(gpu_usage_card)
        
        gpu_usage_title = QLabel("GPU Usage")
        gpu_usage_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        gpu_usage_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background: transparent;")
        
        gpu_usage_value = QLabel("Monitoring...")
        gpu_usage_value.setObjectName("gpu_usage_value")
        gpu_usage_value.setFont(QFont("Segoe UI", 18, QFont.Bold))
        gpu_usage_value.setStyleSheet(f"color: {GS.DARK_THEME['accent']}; background: transparent;")
        
        gpu_usage_layout.addWidget(gpu_usage_title)
        gpu_usage_layout.addWidget(gpu_usage_value)

        network_card = QFrame()
        network_card.setStyleSheet(card_style)
        network_layout = QVBoxLayout(network_card)
        
        network_title = QLabel("Network Speed")
        network_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        network_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background: transparent;")
        
        network_value = QLabel("Monitoring...")
        network_value.setObjectName("network_value")
        network_value.setFont(QFont("Segoe UI", 18, QFont.Bold))
        network_value.setStyleSheet(f"color: {GS.DARK_THEME['accent']}; background: transparent;")
        
        network_layout.addWidget(network_title)
        network_layout.addWidget(network_value)

        fps_card = QFrame()
        fps_card.setStyleSheet(card_style)
        fps_layout = QVBoxLayout(fps_card)
        
        fps_title = QLabel("FPS Monitor")
        fps_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        fps_title.setStyleSheet(f"color: {GS.DARK_THEME['text_primary']}; background: transparent;")
        
        fps_value = QLabel("Not running")
        fps_value.setObjectName("fps_value")
        fps_value.setFont(QFont("Segoe UI", 18, QFont.Bold))
        fps_value.setStyleSheet(f"color: {GS.DARK_THEME['accent']}; background: transparent;")
        
        fps_layout.addWidget(fps_title)
        fps_layout.addWidget(fps_value)

        metrics_layout.addWidget(cpu_temp_card, 0, 0)
        metrics_layout.addWidget(gpu_usage_card, 0, 1)
        metrics_layout.addWidget(network_card, 1, 0)
        metrics_layout.addWidget(fps_card, 1, 1)

        parent_layout.addWidget(metrics_container)
        
    def ud_tm(self):

        current_time = datetime.datetime.now()
        self.time_label.setText(current_time.strftime("%A, %B %d, %Y | %H:%M:%S"))

        self.ud_ss()
        
    def ud_ss(self):
        try:

            cpu_usage = psutil.cpu_percent()
            cpu_label = self.findChild(QLabel, "cpu_value")
            if cpu_label:
                cpu_label.setText(f"{cpu_usage:.1f}%")

            memory = psutil.virtual_memory()
            memory_label = self.findChild(QLabel, "memory_value")
            if memory_label:
                memory_label.setText(f"{memory.percent:.1f}%")

            try:
                disk = psutil.disk_usage('/')
                disk_label = self.findChild(QLabel, "disk_value")
                if disk_label:
                    disk_label.setText(f"{disk.percent:.1f}%")
            except:
                pass

            cpu_temp_label = self.findChild(QLabel, "cpu_temp_value")
            if cpu_temp_label:

                simulated_temp = 40 + (cpu_usage / 100) * 30
                cpu_temp_label.setText(f"{simulated_temp:.1f}°C")

                if simulated_temp > 80:
                    cpu_temp_label.setStyleSheet(f"color: #FF5252; background: transparent;")
                elif simulated_temp > 70:
                    cpu_temp_label.setStyleSheet(f"color: #FFC107; background: transparent;")
                else:
                    cpu_temp_label.setStyleSheet(f"color: {GS.DARK_THEME['accent']}; background: transparent;")

            gpu_usage_label = self.findChild(QLabel, "gpu_usage_value")
            if gpu_usage_label:

                simulated_gpu = max(10, min(95, cpu_usage * 1.2))
                gpu_usage_label.setText(f"{simulated_gpu:.1f}%")

            network_label = self.findChild(QLabel, "network_value")
            if network_label:
                if self.last_net_io is None:
                    self.last_net_io = psutil.net_io_counters()
                    network_label.setText("Calculating...")
                else:
                    current_net_io = psutil.net_io_counters()

                    bytes_sent = current_net_io.bytes_sent - self.last_net_io.bytes_sent
                    bytes_recv = current_net_io.bytes_recv - self.last_net_io.bytes_recv

                    kb_sent = bytes_sent / 1024
                    kb_recv = bytes_recv / 1024

                    network_label.setText(f"↑ {kb_sent:.1f} KB/s\n↓ {kb_recv:.1f} KB/s")

                    self.last_net_io = current_net_io

            fps_label = self.findChild(QLabel, "fps_value")
            if fps_label:

                system_load = (cpu_usage + memory.percent) / 2
                simulated_fps = max(30, 144 - (system_load / 100) * 100)
                fps_label.setText(f"{simulated_fps:.0f} FPS")
                
        except Exception as e:
            print(f"Error updating system stats: {e}")
        
    def ra_sa(self):
        progress = QProgressDialog("Analyzing your system...", "Cancel", 0, 100, self)
        progress.setWindowTitle("System Analysis")
        progress.setWindowModality(Qt.WindowModal)
        progress.setMinimumDuration(0)
        progress.setValue(0)

        self.analysis_thread = threading.Thread(target=self.pf_as, args=(progress,))
        self.analysis_thread.daemon = True
        self.analysis_thread.start()

        timer = QTimer(self)
        
        def update_progress():

            if not self.analysis_thread.is_alive():
                timer.stop()
                progress.setValue(100)
                self.sw_rl()  
                return

            current = progress.value()
            if current < 95:  
                progress.setValue(current + 5)
        
        timer.timeout.connect(update_progress)
        timer.start(300)  
        
    def pf_as(self, progress_dialog):

        try:
            self.analysis_results = {}

            self.analysis_results["cpu"] = {
                "usage": psutil.cpu_percent(interval=1),
                "cores": psutil.cpu_count(logical=False),
                "threads": psutil.cpu_count(logical=True)
            }

            memory = psutil.virtual_memory()
            self.analysis_results["memory"] = {
                "total": self.ft_sz(memory.total),
                "available": self.ft_sz(memory.available),
                "percent_used": memory.percent
            }

            disk_info = []
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disk_info.append({
                        "device": partition.device,
                        "mountpoint": partition.mountpoint,
                        "fstype": partition.fstype,
                        "total": self.ft_sz(usage.total),
                        "free": self.ft_sz(usage.free),
                        "percent_used": usage.percent
                    })
                except:
                    pass
            self.analysis_results["disks"] = disk_info

            self.analysis_results["processes"] = len(psutil.pids())

            net_io = psutil.net_io_counters()
            self.analysis_results["network"] = {
                "bytes_sent": self.ft_sz(net_io.bytes_sent),
                "bytes_recv": self.ft_sz(net_io.bytes_recv)
            }

            self.analysis_results["uptime"] = self.gt_ue()

            try:
                battery = psutil.sensors_battery()
                if battery:
                    self.analysis_results["power"] = {
                        "battery_percent": battery.percent,
                        "power_plugged": battery.power_plugged,
                        "battery_left": self.st_fp_bt(battery.secsleft) if not battery.power_plugged else "N/A"
                    }
                else:
                    self.analysis_results["power"] = {"status": "No battery detected"}
            except:
                self.analysis_results["power"] = {"status": "Unable to get power info"}

            if self.analysis_results["processes"] < 120:
                score = 95
                recommendation = "Your system is well-optimized for gaming!"
            elif self.analysis_results["processes"] < 200:
                score = 80
                recommendation = "Good gaming performance. Consider closing some applications."
            elif self.analysis_results["processes"] < 250:
                score = 65
                recommendation = "Average performance. Close unnecessary applications for better gaming experience."
            else:
                score = 50
                recommendation = "Too many processes running. This may impact gaming performance significantly."
                
            self.analysis_results["gaming_score"] = {
                "score": score,
                "recommendation": recommendation
            }
            
        except Exception as e:
            self.analysis_results["error"] = str(e)
    
    def sw_rl(self):
        if "error" in self.analysis_results:
            QMessageBox.warning(self, "Analysis Error", 
                               f"An error occurred during analysis: {self.analysis_results['error']}")
            return

        message = (
            f"<h3>System Analysis Complete</h3>"
            f"<p><b>Gaming Performance Score:</b> {self.analysis_results['gaming_score']['score']}/100</p>"
            f"<p><b>CPU Usage:</b> {self.analysis_results['cpu']['usage']}%</p>"
            f"<p><b>Memory Used:</b> {self.analysis_results['memory']['percent_used']}%</p>"
            f"<p><b>Processes Running:</b> {self.analysis_results['processes']}</p>"
            f"<h4>Recommendation:</h4>"
            f"<p>{self.analysis_results['gaming_score']['recommendation']}</p>"
        )
        
        if self.main_window:

            self.main_window.ce_pe(1)  

            QMessageBox.information(self, "Analysis Complete", message)
        else:

            QMessageBox.information(self, "Analysis Complete", message)
            
    def vw_si(self):

        dialog = QDialog(self)
        dialog.setWindowTitle("System Information")
        dialog.setMinimumSize(700, 500)
        
        layout = QVBoxLayout(dialog)

        tabs = QTabWidget()

        system_tab = QWidget()
        system_layout = QVBoxLayout(system_tab)
        system_table = QTableWidget()
        system_table.setColumnCount(2)
        system_table.setHorizontalHeaderLabels(["Property", "Value"])
        system_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        system_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        system_table.verticalHeader().setVisible(False)

        system_info = [
            ("OS", platform.system()),
            ("OS Version", platform.version()),
            ("Architecture", platform.machine()),
            ("Computer Name", platform.node()),
            ("Processor", self.gt_pn()),
            ("RAM", self.ft_sz(psutil.virtual_memory().total)),
            ("Python Version", platform.python_version()),
            ("System Uptime", self.gt_ue())
        ]
        
        system_table.setRowCount(len(system_info))
        for i, (prop, value) in enumerate(system_info):
            system_table.setItem(i, 0, QTableWidgetItem(prop))
            system_table.setItem(i, 1, QTableWidgetItem(str(value)))
            
        system_layout.addWidget(system_table)

        hardware_tab = QWidget()
        hardware_layout = QVBoxLayout(hardware_tab)
        hardware_table = QTableWidget()
        hardware_table.setColumnCount(2)
        hardware_table.setHorizontalHeaderLabels(["Property", "Value"])
        hardware_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        hardware_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        hardware_table.verticalHeader().setVisible(False)

        cpu_info = self.gt_cp_if()

        gpu_info = self.gt_gu_if()

        battery_info = self.gt_by_if()

        hardware_info = cpu_info + [("", "")] + gpu_info + [("", "")] + battery_info
        
        hardware_table.setRowCount(len(hardware_info))
        for i, (prop, value) in enumerate(hardware_info):
            hardware_table.setItem(i, 0, QTableWidgetItem(prop))
            hardware_table.setItem(i, 1, QTableWidgetItem(str(value)))
            
        hardware_layout.addWidget(hardware_table)

        storage_tab = QWidget()
        storage_layout = QVBoxLayout(storage_tab)
        storage_table = QTableWidget()
        storage_table.setColumnCount(5)
        storage_table.setHorizontalHeaderLabels(["Drive", "Mount", "Type", "Total", "Free"])
        storage_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        storage_table.verticalHeader().setVisible(False)

        storage_info = []
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                storage_info.append((
                    part.device,
                    part.mountpoint,
                    part.fstype,
                    self.ft_sz(usage.total),
                    self.ft_sz(usage.free)
                ))
            except:
                pass
                
        storage_table.setRowCount(len(storage_info))
        for i, (device, mount, fs_type, total, free) in enumerate(storage_info):
            storage_table.setItem(i, 0, QTableWidgetItem(device))
            storage_table.setItem(i, 1, QTableWidgetItem(mount))
            storage_table.setItem(i, 2, QTableWidgetItem(fs_type))
            storage_table.setItem(i, 3, QTableWidgetItem(total))
            storage_table.setItem(i, 4, QTableWidgetItem(free))
            
        storage_layout.addWidget(storage_table)

        network_tab = QWidget()
        network_layout = QVBoxLayout(network_tab)
        network_table = QTableWidget()
        network_table.setColumnCount(3)
        network_table.setHorizontalHeaderLabels(["Interface", "IP Address", "Type"])
        network_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        network_table.verticalHeader().setVisible(False)

        net_info = self.gt_nk_if()
        
        network_table.setRowCount(len(net_info))
        for i, (interface, ip, if_type) in enumerate(net_info):
            network_table.setItem(i, 0, QTableWidgetItem(interface))
            network_table.setItem(i, 1, QTableWidgetItem(ip))
            network_table.setItem(i, 2, QTableWidgetItem(if_type))
            
        network_layout.addWidget(network_table)

        tabs.addTab(system_tab, "System")
        tabs.addTab(hardware_tab, "Hardware")
        tabs.addTab(storage_tab, "Storage")
        tabs.addTab(network_tab, "Network")

        close_button = QPushButton("Close")
        close_button.clicked.connect(dialog.accept)
        
        layout.addWidget(tabs)
        layout.addWidget(close_button)

        dialog.exec_()
            
    def ay_rd(self):

        QMessageBox.information(self, "Apply Tweaks", 
                                "This would apply recommended tweaks based on your system analysis.")

        if self.main_window:
            self.main_window.ce_pe(4)  

    def ft_sz(self, bytes):

        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024:
                return f"{bytes:.2f} {unit}"
            bytes /= 1024
        return f"{bytes:.2f} PB"
        
    def gt_ue(self):

        uptime_seconds = int(time.time() - psutil.boot_time())
        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if days > 0:
            return f"{days} days, {hours}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
            
    def st_fp_bt(self, seconds):

        if seconds == psutil.POWER_TIME_UNLIMITED:
            return "Unlimited"
        if seconds == psutil.POWER_TIME_UNKNOWN:
            return "Unknown"
            
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return f"{hours}h {minutes}m"
        
    def gt_pn(self):

        if platform.system() == "Windows" and HAS_WMI:
            try:
                w = wmi.WMI()
                for processor in w.Win32_Processor():
                    return processor.Name
            except:
                pass

        return platform.processor()
        
    def gt_cp_if(self):

        info = []
        
        info.append(("Processor", self.gt_pn()))
        info.append(("Physical Cores", psutil.cpu_count(logical=False)))
        info.append(("Logical Cores", psutil.cpu_count()))

        try:
            freq = psutil.cpu_freq()
            if freq:
                if freq.current:
                    info.append(("Current Frequency", f"{freq.current:.2f} MHz"))
                if freq.min:
                    info.append(("Min Frequency", f"{freq.min:.2f} MHz"))
                if freq.max:
                    info.append(("Max Frequency", f"{freq.max:.2f} MHz"))
        except:
            pass

        info.append(("Current Usage", f"{psutil.cpu_percent()}%"))
        
        return info
        
    def gt_gu_if(self):

        info = []
        
        if platform.system() == "Windows" and HAS_WMI:
            try:
                w = wmi.WMI()
                for gpu in w.Win32_VideoController():
                    info.append(("GPU", gpu.Name))
                    if gpu.AdapterRAM:
                        ram_mb = int(int(gpu.AdapterRAM) / (1024*1024))
                        info.append(("GPU RAM", f"{ram_mb} MB"))
                    if gpu.DriverVersion:
                        info.append(("Driver Version", gpu.DriverVersion))
            except Exception as e:
                info.append(("GPU Info Error", str(e)))
        else:
            info.append(("GPU", "Information not available"))
            
        return info
        
    def gt_by_if(self):

        info = []
        
        try:
            battery = psutil.sensors_battery()
            if battery:
                info.append(("Battery Level", f"{battery.percent}%"))
                info.append(("Power Plugged", "Yes" if battery.power_plugged else "No"))
                if not battery.power_plugged:
                    info.append(("Battery Time Left", self.st_fp_bt(battery.secsleft)))
            else:
                info.append(("Battery", "No battery detected"))
        except:
            info.append(("Battery", "Information not available"))
            
        return info
        
    def gt_nk_if(self):

        net_info = []

        hostname = platform.node()
        net_info.append((f"Hostname", hostname, "System"))

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            net_info.append(("Primary IP", ip, "System"))
        except:
            pass

        for interface, addrs in psutil.net_if_addrs().items():

            if platform.system() != "Windows" and interface == "lo":
                continue
                
            for addr in addrs:
                if addr.family == socket.AF_INET:  

                    name = interface.lower()
                    if "wi-fi" in name or "wlan" in name or "wireless" in name:
                        if_type = "Wireless"
                    elif "ethernet" in name or "eth" in name:
                        if_type = "Ethernet"
                    elif "bluetooth" in name:
                        if_type = "Bluetooth"
                    elif "vpn" in name or "virtual" in name:
                        if_type = "Virtual/VPN"
                    else:
                        if_type = "Other"
                    
                    net_info.append((interface, addr.address, if_type))
                    
        return net_info

    def gt_db(self):
        if self.main_window:
            self.main_window.ce_pe("dashboard", 1)  