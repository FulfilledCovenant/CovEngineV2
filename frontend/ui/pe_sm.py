from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTabWidget,
                               QTableWidget, QTableWidgetItem, QHBoxLayout,
                               QPushButton, QFrame, QHeaderView, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
import platform
import psutil
import os
import datetime
import time
import subprocess
import re
import socket

try:
    if platform.system() == "Windows":
        import wmi
        import ctypes
        HAS_WMI = True
    else:
        HAS_WMI = False
except ImportError:
    HAS_WMI = False

try:
    import netifaces
    HAS_NETIFACES = True
except ImportError:
    HAS_NETIFACES = False

class SM(QWidget):
    def __init__(self, backend=None):
        super().__init__()

        self.backend = backend

        if platform.system() == "Windows" and HAS_WMI:
            self.wmi_client = wmi.WMI()
        else:
            self.wmi_client = None

        self.stUI()

    def stUI(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        header_label = QLabel("System Information")
        header_font = QFont()
        header_font.setPointSize(18)
        header_font.setBold(True)
        header_label.setFont(header_font)

        action_layout = QHBoxLayout()

        refresh_btn = QPushButton("Refresh Data")
        refresh_btn.clicked.connect(self.rf_dt)

        export_btn = QPushButton("Export Data")
        export_btn.clicked.connect(self.ep_dt)

        action_layout.addStretch()
        action_layout.addWidget(refresh_btn)
        action_layout.addWidget(export_btn)

        self.tabs = QTabWidget()

        self.sys_info_tab = QWidget()
        self.hardware_tab = QWidget()
        self.storage_tab = QWidget()
        self.network_tab = QWidget()

        self.tabs.addTab(self.sys_info_tab, "System")
        self.tabs.addTab(self.hardware_tab, "Hardware")
        self.tabs.addTab(self.storage_tab, "Storage")
        self.tabs.addTab(self.network_tab, "Network")

        self.ie_st()
        self.ie_hw()
        self.ie_sg()
        self.ie_nw()

        main_layout.addWidget(header_label)
        main_layout.addLayout(action_layout)
        main_layout.addWidget(self.tabs)

    def ie_st(self):
        layout = QVBoxLayout(self.sys_info_tab)

        desc_label = QLabel("Basic system information and operating system details")
        layout.addWidget(desc_label)

        self.system_table = QTableWidget()
        self.system_table.setColumnCount(2)
        self.system_table.setHorizontalHeaderLabels(["Property", "Value"])
        self.system_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.system_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.system_table.setAlternatingRowColors(True)
        self.system_table.verticalHeader().setVisible(False)

        self.ud_si()

        layout.addWidget(self.system_table)

    def ie_hw(self):
        layout = QVBoxLayout(self.hardware_tab)

        desc_label = QLabel("CPU, memory, and other hardware specifications")
        layout.addWidget(desc_label)

        self.hardware_table = QTableWidget()
        self.hardware_table.setColumnCount(2)
        self.hardware_table.setHorizontalHeaderLabels(["Property", "Value"])
        self.hardware_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.hardware_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.hardware_table.setAlternatingRowColors(True)
        self.hardware_table.verticalHeader().setVisible(False)

        self.ud_hw()

        layout.addWidget(self.hardware_table)

    def ie_sg(self):
        layout = QVBoxLayout(self.storage_tab)

        desc_label = QLabel("Disk drives and storage information")
        layout.addWidget(desc_label)

        self.storage_table = QTableWidget()
        self.storage_table.setColumnCount(5)
        self.storage_table.setHorizontalHeaderLabels(["Drive", "Mount", "Type", "Total", "Free Space"])
        self.storage_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.storage_table.setAlternatingRowColors(True)
        self.storage_table.verticalHeader().setVisible(False)

        self.ud_sg()

        layout.addWidget(self.storage_table)

    def ie_nw(self):
        layout = QVBoxLayout(self.network_tab)

        desc_label = QLabel("Network interfaces and connectivity information")
        layout.addWidget(desc_label)

        self.network_table = QTableWidget()
        self.network_table.setColumnCount(3)
        self.network_table.setHorizontalHeaderLabels(["Interface", "IP Address", "Type"])
        self.network_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.network_table.setAlternatingRowColors(True)
        self.network_table.verticalHeader().setVisible(False)

        self.ud_nw()

        layout.addWidget(self.network_table)

    def ud_si(self):
        try:
            if self.backend:
                data = self.backend.gt_sy()
                system_info = [
                    ("Operating System", data.get("os", platform.system() + " " + platform.release())),
                    ("OS Version", data.get("version", platform.version())),
                    ("System Name", data.get("hostname", platform.node())),
                    ("Architecture", data.get("architecture", platform.machine())),
                    ("Python Version", platform.python_version()),
                    ("System Uptime", self.get_uptime()),
                    ("User", os.getlogin()),
                    ("Current Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                    ("Time Zone", datetime.datetime.now().astimezone().tzname()),
                ]
            else:
                system_info = [
                    ("Operating System", platform.system() + " " + platform.release()),
                    ("OS Version", platform.version()),
                    ("System Name", platform.node()),
                    ("Architecture", platform.machine()),
                    ("Python Version", platform.python_version()),
                    ("System Uptime", self.get_uptime()),
                    ("User", os.getlogin()),
                    ("Current Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                    ("Time Zone", datetime.datetime.now().astimezone().tzname()),
                ]

            self.system_table.setRowCount(len(system_info))

            for row, (prop, value) in enumerate(system_info):
                self.system_table.setItem(row, 0, QTableWidgetItem(prop))
                self.system_table.setItem(row, 1, QTableWidgetItem(str(value)))
        except Exception as e:
            print(f"Error updating system info: {e}")

    def ud_hw(self):
        try:
            processor_name = self.get_processor_name()
            physical_cores, logical_cores = self.get_cpu_cores()
            cpu_speed = self.get_cpu_speed()

            mem = psutil.virtual_memory()
            swap = psutil.swap_memory()

            total_mem_gb = mem.total / (1024**3)
            total_swap_gb = swap.total / (1024**3)

            gpu_info = self.get_gpu_info()

            hardware_info = [
                ("Processor", processor_name),
                ("CPU Speed", cpu_speed),
                ("Physical CPU Cores", physical_cores),
                ("Logical CPU Cores", logical_cores),
                ("Total RAM", f"{total_mem_gb:.2f} GB"),
                ("Total Swap", f"{total_swap_gb:.2f} GB"),
                ("GPU", gpu_info),
                ("Battery", self.get_battery_info()),
            ]

            self.hardware_table.setRowCount(len(hardware_info))

            for row, (prop, value) in enumerate(hardware_info):
                self.hardware_table.setItem(row, 0, QTableWidgetItem(prop))
                self.hardware_table.setItem(row, 1, QTableWidgetItem(str(value)))
        except Exception as e:
            print(f"Error updating hardware info: {e}")

    def ud_sg(self):
        try:
            disks = []

            if platform.system() == "Windows" and HAS_WMI:
                try:
                    physical_disks = {}
                    for disk in self.wmi_client.Win32_DiskDrive():
                        if disk.Model:
                            physical_disks[disk.DeviceID] = {
                                "model": disk.Model,
                                "size": float(disk.Size) if disk.Size else 0
                            }

                    for partition in self.wmi_client.Win32_LogicalDisk():
                        if partition.DriveType in (2, 3):
                            try:
                                device = partition.DeviceID
                                mount = partition.DeviceID
                                fs_type = partition.FileSystem or "Unknown"
                                total_bytes = float(partition.Size) if partition.Size else 0
                                free_bytes = float(partition.FreeSpace) if partition.FreeSpace else 0

                                total = self.format_size(total_bytes)
                                free = self.format_size(free_bytes)

                                disks.append((device, mount, fs_type, total, free))
                            except Exception as e:
                                print(f"Error getting WMI logical disk info: {e}")
                except Exception as e:
                    print(f"Error during WMI disk detection: {e}")

            if not disks:
                for part in psutil.disk_partitions(all=False):
                    if platform.system() == "Windows" and "cdrom" in part.opts.lower():
                        continue

                    if platform.system() != "Windows":
                        if part.fstype in ('tmpfs', 'devtmpfs', 'devfs', 'overlay', 'aufs', 'squashfs'):
                            continue

                    try:
                        usage = psutil.disk_usage(part.mountpoint)

                        device = part.device
                        if platform.system() == "Windows" and device.endswith('\\'):
                            device = device[:-1]

                        disks.append((
                            device,
                            part.mountpoint,
                            part.fstype,
                            self.format_size(usage.total),
                            self.format_size(usage.free)
                        ))
                    except PermissionError:
                        disks.append((
                            part.device,
                            part.mountpoint,
                            part.fstype,
                            "Access Denied",
                            "Access Denied"
                        ))
                    except Exception as e:
                        print(f"Error getting disk info for {part.mountpoint}: {e}")

            if not disks:
                if platform.system() == "Windows":
                    try:
                        import string
                        available_drives = []
                        for drive in string.ascii_uppercase:
                            if os.path.exists(f"{drive}:"):
                                try:
                                    usage = psutil.disk_usage(f"{drive}:")
                                    available_drives.append((
                                        f"{drive}:",
                                        f"{drive}:",
                                        "Unknown",
                                        self.format_size(usage.total),
                                        self.format_size(usage.free)
                                    ))
                                except:
                                    available_drives.append((
                                        f"{drive}:",
                                        f"{drive}:",
                                        "Unknown",
                                        "Unknown",
                                        "Unknown"
                                    ))
                        disks = available_drives
                    except Exception as e:
                        print(f"Error in last resort Windows disk detection: {e}")

                elif platform.system() == "Linux":
                    try:
                        with open('/proc/mounts', 'r') as f:
                            for line in f:
                                parts = line.split()
                                if len(parts) >= 2:
                                    device = parts[0]
                                    mountpoint = parts[1]
                                    fs_type = parts[2] if len(parts) > 2 else "Unknown"

                                    if any(x in device for x in ['/dev/loop', 'tmpfs', 'devtmpfs', 'udev']):
                                        continue

                                    try:
                                        usage = psutil.disk_usage(mountpoint)
                                        disks.append((
                                            device,
                                            mountpoint,
                                            fs_type,
                                            self.format_size(usage.total),
                                            self.format_size(usage.free)
                                        ))
                                    except:
                                        disks.append((
                                            device,
                                            mountpoint,
                                            fs_type,
                                            "Unknown",
                                            "Unknown"
                                        ))
                    except Exception as e:
                        print(f"Error in last resort Linux disk detection: {e}")

            self.storage_table.setRowCount(len(disks))

            for row, (device, mount, fs_type, total, free) in enumerate(disks):
                self.storage_table.setItem(row, 0, QTableWidgetItem(device))
                self.storage_table.setItem(row, 1, QTableWidgetItem(mount))
                self.storage_table.setItem(row, 2, QTableWidgetItem(fs_type))
                self.storage_table.setItem(row, 3, QTableWidgetItem(total))
                self.storage_table.setItem(row, 4, QTableWidgetItem(free))

        except Exception as e:
            print(f"Error updating storage info: {e}")

    def format_size(self, size_bytes):
        if not isinstance(size_bytes, (int, float)) or size_bytes == 0:
            return "Unknown"

        units = ["B", "KB", "MB", "GB", "TB", "PB"]
        size = float(size_bytes)
        unit_index = 0

        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1

        if unit_index == 0:
            return f"{int(size)} {units[unit_index]}"
        else:
            return f"{size:.2f} {units[unit_index]}"

    def ud_nw(self):
        try:
            net_info = []

            hostname = socket.gethostname()
            host_ip = None
            try:
                host_ip = socket.gethostbyname(hostname)
                if host_ip == "127.0.0.1" or host_ip == "::1":
                    host_ip = self.get_primary_ip()
            except:
                host_ip = self.get_primary_ip()

            net_info.append(("Hostname", hostname, "System"))
            if host_ip:
                net_info.append(("Primary IP", host_ip, "System"))

            if HAS_NETIFACES:
                for interface in netifaces.interfaces():
                    if interface == "lo" or interface == "localhost":
                        continue

                    addresses = netifaces.ifaddresses(interface)

                    if netifaces.AF_INET in addresses:
                        for addr_info in addresses[netifaces.AF_INET]:
                            ip = addr_info.get('addr')
                            if ip:
                                if_type = self.determine_interface_type(interface)
                                net_info.append((interface, ip, if_type))


            else:
                net_if_addrs = psutil.net_if_addrs()
                for interface, addresses in net_if_addrs.items():
                    if (platform.system() != "Windows" and interface == "lo") or "loopback" in interface.lower():
                        continue

                    for addr in addresses:
                        if addr.family == socket.AF_INET:
                            ip_address = addr.address
                            if_type = self.determine_interface_type(interface)
                            net_info.append((interface, ip_address, if_type))
                            break

            if HAS_NETIFACES:
                for interface in netifaces.interfaces():
                    if interface == "lo" or interface == "localhost":
                        continue

                    addresses = netifaces.ifaddresses(interface)
                    if netifaces.AF_LINK in addresses:
                        for addr_info in addresses[netifaces.AF_LINK]:
                            mac = addr_info.get('addr')
                            if mac:
                                net_info.append((f"{interface} MAC", mac, "Hardware"))

            self.network_table.setRowCount(len(net_info))

            for row, (interface, ip, if_type) in enumerate(net_info):
                self.network_table.setItem(row, 0, QTableWidgetItem(interface))
                self.network_table.setItem(row, 1, QTableWidgetItem(ip))
                self.network_table.setItem(row, 2, QTableWidgetItem(if_type))

        except Exception as e:
            print(f"Error updating network info: {e}")

    def get_processor_name(self):
        try:
            if platform.system() == "Windows":
                if HAS_WMI:
                    for processor in self.wmi_client.Win32_Processor():
                        return processor.Name

                processor = platform.processor()
                if processor:
                    processor = re.sub(r'\s+', ' ', processor)
                    processor = re.sub(r'CPU|Processor', '', processor)
                    return processor.strip()

            elif platform.system() == "Linux":
                try:
                    with open('/proc/cpuinfo', 'r') as f:
                        for line in f:
                            if line.startswith('model name'):
                                return line.split(':')[1].strip()
                except:
                    pass

                try:
                    output = subprocess.check_output("lscpu", universal_newlines=True)
                    for line in output.split('\n'):
                        if "Model name" in line:
                            return line.split(':')[1].strip()
                except:
                    pass

            elif platform.system() == "Darwin":
                try:
                    output = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"], universal_newlines=True)
                    return output.strip()
                except:
                    pass
        except Exception as e:
            print(f"Error getting processor name: {e}")

        return platform.processor() or "Unknown"

    def get_cpu_cores(self):
        try:
            physical = psutil.cpu_count(logical=False) or 0
            logical = psutil.cpu_count(logical=True) or 0

            if platform.system() == "Windows" and HAS_WMI:
                try:
                    cores = 0
                    for processor in self.wmi_client.Win32_Processor():
                        cores += int(processor.NumberOfCores)
                    if cores > 0:
                        physical = cores
                except:
                    pass

            return physical, logical
        except:
            return psutil.cpu_count(logical=False) or 0, psutil.cpu_count(logical=True) or 0

    def get_cpu_speed(self):
        try:
            freq = psutil.cpu_freq()
            if freq and freq.max:
                return f"{freq.max / 1000:.2f} GHz"

            if platform.system() == "Windows":
                if HAS_WMI:
                    for processor in self.wmi_client.Win32_Processor():
                        return f"{processor.MaxClockSpeed / 1000:.2f} GHz"

            elif platform.system() == "Linux":
                try:
                    with open('/proc/cpuinfo', 'r') as f:
                        for line in f:
                            if line.startswith('cpu MHz'):
                                mhz = float(line.split(':')[1].strip())
                                return f"{mhz / 1000:.2f} GHz"
                except:
                    pass

                try:
                    output = subprocess.check_output("lscpu", universal_newlines=True)
                    for line in output.split('\n'):
                        if "CPU max MHz" in line:
                            mhz = float(line.split(':')[1].strip())
                            return f"{mhz / 1000:.2f} GHz"
                except:
                    pass

            elif platform.system() == "Darwin":
                try:
                    output = subprocess.check_output(["sysctl", "-n", "hw.cpufrequency_max"], universal_newlines=True)
                    return f"{int(output.strip()) / 1000000000:.2f} GHz"
                except:
                    pass
        except Exception as e:
            print(f"Error getting CPU speed: {e}")

        return "Unknown"

    def get_gpu_info(self):
        try:
            if platform.system() == "Windows" and HAS_WMI:
                gpu_list = []
                for gpu in self.wmi_client.Win32_VideoController():
                    if gpu.Name:
                        gpu_list.append(gpu.Name)
                if gpu_list:
                    return ", ".join(gpu_list)

            elif platform.system() == "Linux":
                try:
                    output = subprocess.check_output("lspci | grep -i 'vga\|3d\|2d'", shell=True, universal_newlines=True)
                    if output:
                        gpus = []
                        for line in output.strip().split('\n'):
                            match = re.search(r":\s(.*)\[", line)
                            if match:
                                gpus.append(match.group(1).strip())
                            else:
                                parts = line.split(":")
                                if len(parts) > 1:
                                    gpus.append(parts[1].strip())
                        if gpus:
                            return ", ".join(gpus)
                except:
                    pass
        except Exception as e:
            print(f"Error getting GPU info: {e}")

        return "Information not available"

    def get_uptime(self):
        try:
            uptime_seconds = int(time.time() - psutil.boot_time())

            days, remainder = divmod(uptime_seconds, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)

            uptime_str = ""
            if days > 0:
                uptime_str += f"{days} days, "

            uptime_str += f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            return uptime_str
        except:
            return "Unknown"

    def get_battery_info(self):
        try:
            battery = psutil.sensors_battery()
            if battery:
                percent = battery.percent
                power_plugged = battery.power_plugged

                status = "Charging" if power_plugged else "Discharging"
                return f"{percent}% ({status})"
            else:
                return "No battery detected"
        except:
            return "Not available"

    def get_primary_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "Unable to determine"

    def determine_interface_type(self, interface_name):
        name = interface_name.lower()

        if "wi-fi" in name or "wlan" in name or "wireless" in name:
            return "Wireless"
        elif "ethernet" in name or "eth" in name or name.startswith("en"):
            return "Ethernet"
        elif "bluetooth" in name or "bt" in name:
            return "Bluetooth"
        elif "vpn" in name or "virtual" in name or "vbox" in name:
            return "Virtual/VPN"
        elif "mobile" in name or "rmnet" in name or "ppp" in name:
            return "Mobile"
        elif "lo" in name:
            return "Loopback"

        try:
            stats = psutil.net_if_stats()
            if interface_name in stats:
                if stats[interface_name].isup:
                    return "Active Interface"
                else:
                    return "Inactive Interface"
        except:
            pass

        return "Other"

    def rf_dt(self):
        print("Refreshing system information...")

        try:
            self.ud_si()
            self.ud_hw()
            self.ud_sg()
            self.ud_nw()

            QApplication.processEvents()

            print("System information refresh complete")
        except Exception as e:
            print(f"Error refreshing system information: {e}")

    def ep_dt(self):
        print("Exporting system information...")
