import os
import subprocess
import winreg
import ctypes
import logging
import json
from typing import List, Dict, Any, Union
import sys
import tempfile

class TM:
    
    def __init__(self):
        self.logger = logging.getLogger("TweakManager")
        self.backend_path = self._get_backend_path()
        
    def _get_backend_path(self) -> str:
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
            backend_path = os.path.join(base_path, "backend", "build", "Release", "CEV2.exe")
        else:
            base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            backend_path = os.path.join(base_path, "backend", "build", "Release", "CEV2.exe")
        
        if not os.path.exists(backend_path):
            self.logger.warning(f"Backend executable not found at: {backend_path}")
            alt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CEV2.exe")
            if os.path.exists(alt_path):
                backend_path = alt_path
                self.logger.info(f"Found backend at alternative path: {backend_path}")
        
        return backend_path
    
    def ce_rp(self) -> Dict[str, Any]:
        self.logger.info("Creating system restore point before applying tweaks")
        
        try:
            if getattr(sys, 'frozen', False):
                base_path = os.path.dirname(sys.executable)
            else:
                base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
                
            batch_file = os.path.join(base_path, "create_restore_point.bat")
            
            if not os.path.exists(batch_file):
                self.logger.warning(f"Batch file not found at: {batch_file}, creating it")
                with open(batch_file, "w") as f:
                    f.write('@echo off\n')
                    f.write('echo Creating system restore point...\n')
                    f.write('powershell -Command __STRING_PLACEHOLDER_35__\n')
                    f.write('if %errorlevel% equ 0 (\n')
                    f.write('    echo System restore point created successfully.\n')
                    f.write('    exit /b 0\n')
                    f.write(') else (\n')
                    f.write('    echo Failed to create system restore point.\n')
                    f.write('    exit /b 1\n')
                    f.write(')')
            
            if os.name == 'nt':
                result = ctypes.windll.shell32.ShellExecuteW(
                    None, 
                    "runas", 
                    batch_file,
                    None, 
                    None, 
                    1  
                )
                
                if result > 32:
                    self.logger.info("System restore point creation initiated")
                    return {"success": True, "message": "System restore point creation initiated"}
                else:
                    self.logger.error(f"Failed to run batch file as admin: {result}")
                    return {"success": False, "message": f"Failed to run batch file as admin: {result}"}
            else:
                cmd = "powershell -Command \"Checkpoint-Computer -Description 'CovEngineV2 Tweaks' -RestorePointType 'APPLICATION_INSTALL'\""
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                
                if result.returncode == 0:
                    self.logger.info("System restore point created successfully")
                    return {"success": True, "message": "System restore point created successfully"}
                else:
                    self.logger.error(f"Failed to create system restore point: {result.stderr}")
                    return {"success": False, "message": f"Failed to create system restore point: {result.stderr}"}
                    
        except Exception as e:
            self.logger.error(f"Error creating system restore point: {str(e)}")
            return {"success": False, "message": f"Error creating system restore point: {str(e)}"}
    
    def ay_ts(self, tweaks: Dict[str, List[str]], create_restore_point: bool = True) -> Dict[str, Any]:

        results = {
            "successful": [],
            "failed": [],
            "skipped": [],
            "requires_restart": False
        }
        
        if create_restore_point:
            restore_result = self.ce_rp()
            if not restore_result.get("success", False):
                self.logger.warning(f"Failed to create system restore point: {restore_result.get('message', 'Unknown error')}")
        
        backend_tweaks = []
        for category, tweak_ids in tweaks.items():
            for tweak_id in tweak_ids:
                backend_tweaks.append({"id": tweak_id, "category": category})
        
        if not backend_tweaks:
            self.logger.warning("No tweaks selected for application")
            return results
        
        try:

            backend_results = self._call_backend_apply_tweaks(backend_tweaks)

            if "successful" in backend_results:
                results["successful"] = backend_results["successful"]
            
            if "failed" in backend_results:
                for failed_tweak in backend_results["failed"]:
                    results["failed"].append({
                        "id": failed_tweak["id"],
                        "reason": failed_tweak.get("reason", "Unknown error")
                    })

            for tweak_id in results["successful"]:
                if self._tweak_requires_restart(tweak_id):
                    results["requires_restart"] = True
                    break
                    
        except Exception as e:
            self.logger.error(f"Error applying tweaks via backend: {str(e)}")

            self.logger.info("Falling back to legacy tweak implementation")
            return self._legacy_apply_tweaks(tweaks)
        
        return results
    
    def _call_backend_apply_tweaks(self, tweaks: List[Dict[str, str]]) -> Dict[str, Any]:
        self.logger.info(f"Calling backend to apply {len(tweaks)} tweaks")

        if not os.path.exists(self.backend_path):
            raise FileNotFoundError(f"Backend executable not found at: {self.backend_path}")

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(tweaks, f)
            temp_file = f.name
        
        try:

            cmd = [self.backend_path, "command", "apply_tweaks", temp_file]
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode != 0:
                raise RuntimeError(f"Backend process error: {result.stderr}")

            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                raise RuntimeError(f"Backend process error: {result.stderr}")
        finally:

            try:
                os.unlink(temp_file)
            except:
                pass
    
    def _tweak_requires_restart(self, tweak_id: str) -> bool:
        restart_tweaks = [
            "configure_bcdedit",
            "disable_memory_compression",
            "disable_pagefile",
            "disable_paging_settings",
            "disable_service_host_splitting",
            "disable_spectre_and_meltdown",
            "disable_core_parking",
            "disable_windows_updates",
            "disable_windows_defender",
            "disable_firewall",
            "disable_smb1",
            "disable_mouse_acceleration"
        ]
        
        return tweak_id in restart_tweaks
    
    def _legacy_apply_tweaks(self, tweaks: Dict[str, List[str]]) -> Dict[str, Any]:
        self.logger.info("Using legacy tweak implementation")
        
        results = {
            "successful": [],
            "failed": [],
            "skipped": [],
            "requires_restart": False
        }

        all_tweaks = []
        for category, tweak_ids in tweaks.items():
            all_tweaks.extend(tweak_ids)

        for tweak_id in all_tweaks:
            try:

                if tweak_id == "disable_memory_compression":
                    result = self.tweak_disable_memory_compression()
                elif tweak_id == "set_ram_usage_high":
                    result = self.tweak_set_ram_usage_high()
                elif tweak_id == "disable_pagefile":
                    result = self.tweak_disable_pagefile()
                elif tweak_id == "disable_mouse_acceleration":
                    result = self.tweak_disable_mouse_acceleration()
                elif tweak_id == "disable_game_bar":
                    result = self.tweak_disable_game_bar()
                elif tweak_id == "disable_telemetry":
                    result = self.tweak_disable_telemetry()
                elif tweak_id == "disable_advertising_id":
                    result = self.tweak_disable_advertising_id()
                elif tweak_id == "disable_smb1":
                    result = self.tweak_disable_smb1()
                elif tweak_id == "enhance_smartscreen":
                    result = self.tweak_enhance_smartscreen()
                else:
                    self.logger.warning(f"No implementation found for tweak: {tweak_id}")
                    results["skipped"].append(tweak_id)
                    continue

                if result.get("success", False):
                    results["successful"].append(tweak_id)

                    if self._tweak_requires_restart(tweak_id):
                        results["requires_restart"] = True
                else:
                    results["failed"].append({
                        "id": tweak_id,
                        "reason": result.get("message", "Unknown error")
                    })
            except Exception as e:
                self.logger.error(f"Error applying tweak {tweak_id}: {str(e)}")
                results["failed"].append({
                    "id": tweak_id,
                    "reason": str(e)
                })
        
        return results
    
    def _rd_me(self, key_path: str, value_name: str, value_type: int, value: Union[str, int, bytes]) -> Dict[str, Any]:
        try:

            root_key_str, subkey = key_path.split('\\', 1)

            root_key_map = {
                'HKEY_CURRENT_USER': winreg.HKEY_CURRENT_USER,
                'HKCU': winreg.HKEY_CURRENT_USER,
                'HKEY_LOCAL_MACHINE': winreg.HKEY_LOCAL_MACHINE,
                'HKLM': winreg.HKEY_LOCAL_MACHINE,
                'HKEY_CLASSES_ROOT': winreg.HKEY_CLASSES_ROOT,
                'HKCR': winreg.HKEY_CLASSES_ROOT,
                'HKEY_USERS': winreg.HKEY_USERS,
                'HKU': winreg.HKEY_USERS
            }
            
            if root_key_str not in root_key_map:
                return {"success": False, "message": f"Invalid root key: {root_key_str}"}
            
            root_key = root_key_map[root_key_str]

            key = winreg.CreateKeyEx(root_key, subkey, 0, winreg.KEY_WRITE)

            winreg.SetValueEx(key, value_name, 0, value_type, value)

            winreg.CloseKey(key)
            
            return {"success": True, "message": f"Successfully set registry value: {key_path}\\{value_name}"}
        except Exception as e:
            return {"success": False, "message": f"Error setting registry value: {str(e)}"}
    
    def _rn_pd(self, cmd: str, shell: bool = True, as_admin: bool = False) -> Dict[str, Any]:
        try:
            if as_admin and os.name == 'nt':

                if isinstance(cmd, list):
                    cmd = ' '.join(cmd)
                
                result = ctypes.windll.shell32.ShellExecuteW(
                    None, 
                    "runas", 
                    cmd,
                    None, 
                    None, 
                    1  
                )

                if result > 32:
                    return {"success": True, "message": "Command executed successfully", "output": ""}
                else:
                    return {"success": False, "message": f"Failed to run command as admin: {result}", "output": ""}
            else:

                result = subprocess.run(cmd, shell=shell, capture_output=True, text=True)
                
                if result.returncode == 0:
                    return {"success": True, "message": "Command executed successfully", "output": result.stdout}
                else:
                    return {"success": False, "message": f"Command failed with exit code: {result.returncode}", "output": result.stderr}
        except Exception as e:
            return {"success": False, "message": f"Error running command: {str(e)}", "output": ""}
    
    def _is_admin(self) -> bool:
        if os.name == 'nt':
            try:
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            except:
                return False
        else:
            return os.geteuid() == 0

    
    def tweak_disable_memory_compression(self) -> Dict[str, Any]:
        self.logger.info("Disabling memory compression")

        return self._rn_pd("powershell -Command \"Disable-MMAgent -MemoryCompression\"", as_admin=True)
    
    def tweak_set_ram_usage_high(self) -> Dict[str, Any]:
        self.logger.info("Setting RAM usage to high")

        result1 = self._rd_me(
            "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
            "LargeSystemCache",
            winreg.REG_DWORD,
            3  
        )

        result2 = self._rd_me(
            "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
            "IoPageLockLimit",
            winreg.REG_DWORD,
            1  
        )
        
        if result1["success"] and result2["success"]:
            return {"success": True, "message": "Successfully set RAM usage to high"}
        else:
            return {"success": False, "message": f"Failed to set RAM usage to high: {result1.get('message', '')} {result2.get('message', '')}"}
    
    def tweak_disable_pagefile(self) -> Dict[str, Any]:
        self.logger.info("Disabling pagefile")
        
        try:

            result = self._rn_pd(
                "powershell -Command \"$computersys = Get-WmiObject Win32_ComputerSystem -EnableAllPrivileges; $computersys.AutomaticManagedPagefile = $False; $computersys.Put()\"",
                as_admin=True
            )
            
            if not result["success"]:
                return result

            result = self._rn_pd(
                "powershell -Command \"$pagefile = Get-WmiObject -Query 'SELECT * FROM Win32_PageFileSetting'; $pagefile.InitialSize = 0; $pagefile.MaximumSize = 0; $pagefile.Put()\"",
                as_admin=True
            )
            
            if not result["success"]:
                return result

            result = self._rd_me(
                "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management",
                "ClearPageFileAtShutdown",
                winreg.REG_DWORD,
                0
            )
            
            if not result["success"]:
                return result
            
            return {"success": True, "message": "Successfully disabled pagefile"}
        except Exception as e:
            return {"success": False, "message": f"Failed to disable pagefile: {str(e)}"}
    
    def tweak_disable_mouse_acceleration(self) -> Dict[str, Any]:
        self.logger.info("Disabling mouse acceleration")

        result1 = self._rd_me(
            "HKEY_CURRENT_USER\\Control Panel\\Mouse",
            "MouseSpeed",
            winreg.REG_SZ,
            "0"
        )

        result2 = self._rd_me(
            "HKEY_CURRENT_USER\\Control Panel\\Mouse",
            "MouseThreshold1",
            winreg.REG_SZ,
            "0"
        )
        
        result3 = self._rd_me(
            "HKEY_CURRENT_USER\\Control Panel\\Mouse",
            "MouseThreshold2",
            winreg.REG_SZ,
            "0"
        )
        
        if result1["success"] and result2["success"] and result3["success"]:
            return {"success": True, "message": "Successfully disabled mouse acceleration"}
        else:
            return {"success": False, "message": f"Failed to disable mouse acceleration: {result1.get('message', '')} {result2.get('message', '')} {result3.get('message', '')}"}
    
    def tweak_disable_game_bar(self) -> Dict[str, Any]:
        self.logger.info("Disabling Game Bar")

        result1 = self._rd_me(
            "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
            "AppCaptureEnabled",
            winreg.REG_DWORD,
            0
        )

        result2 = self._rd_me(
            "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR",
            "GameDVR_Enabled",
            winreg.REG_DWORD,
            0
        )

        result3 = self._rd_me(
            "HKEY_CURRENT_USER\\Software\\Microsoft\\GameBar",
            "ShowStartupPanel",
            winreg.REG_DWORD,
            0
        )

        result4 = self._rd_me(
            "HKEY_CURRENT_USER\\Software\\Microsoft\\GameBar",
            "GamePanelStartupTipIndex",
            winreg.REG_DWORD,
            0
        )
        
        if result1["success"] and result2["success"] and result3["success"] and result4["success"]:
            return {"success": True, "message": "Successfully disabled Game Bar"}
        else:
            return {"success": False, "message": f"Failed to disable Game Bar: {result1.get('message', '')} {result2.get('message', '')} {result3.get('message', '')} {result4.get('message', '')}"}
    
    def tweak_disable_telemetry(self) -> Dict[str, Any]:
        self.logger.info("Disabling telemetry")

        result1 = self._rd_me(
            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection",
            "AllowTelemetry",
            winreg.REG_DWORD,
            0
        )

        result2 = self._rd_me(
            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\SQMClient\\Windows",
            "CEIPEnable",
            winreg.REG_DWORD,
            0
        )

        result3 = self._rd_me(
            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat",
            "AITEnable",
            winreg.REG_DWORD,
            0
        )

        result4 = self._rn_pd("sc config DiagTrack start= disabled", as_admin=True)

        result5 = self._rn_pd("sc config dmwappushservice start= disabled", as_admin=True)
        
        if result1["success"] and result2["success"] and result3["success"] and result4["success"] and result5["success"]:
            return {"success": True, "message": "Successfully disabled telemetry"}
        else:
            return {"success": False, "message": f"Failed to disable telemetry: {result1.get('message', '')} {result2.get('message', '')} {result3.get('message', '')} {result4.get('message', '')} {result5.get('message', '')}"}
    
    def tweak_disable_advertising_id(self) -> Dict[str, Any]:
        self.logger.info("Disabling advertising ID")

        result1 = self._rd_me(
            "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo",
            "Enabled",
            winreg.REG_DWORD,
            0
        )

        result2 = self._rd_me(
            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\AdvertisingInfo",
            "DisabledByGroupPolicy",
            winreg.REG_DWORD,
            1
        )
        
        if result1["success"] and result2["success"]:
            return {"success": True, "message": "Successfully disabled advertising ID"}
        else:
            return {"success": False, "message": f"Failed to disable advertising ID: {result1.get('message', '')} {result2.get('message', '')}"}
    
    def tweak_disable_smb1(self) -> Dict[str, Any]:
        self.logger.info("Disabling SMB1")

        result = self._rn_pd("dism /online /Disable-Feature /FeatureName:SMB1Protocol /NoRestart", as_admin=True)
        
        if result["success"]:
            return {"success": True, "message": "Successfully disabled SMB1"}
        else:
            return {"success": False, "message": f"Failed to disable SMB1: {result.get('message', '')}"}
    
    def tweak_enhance_smartscreen(self) -> Dict[str, Any]:
        self.logger.info("Enhancing SmartScreen")

        result1 = self._rd_me(
            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\System",
            "EnableSmartScreen",
            winreg.REG_DWORD,
            1
        )

        result2 = self._rd_me(
            "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\System",
            "ShellSmartScreenLevel",
            winreg.REG_SZ,
            "Block"
        )
        
        if result1["success"] and result2["success"]:
            return {"success": True, "message": "Successfully enhanced SmartScreen"}
        else:
            return {"success": False, "message": f"Failed to enhance SmartScreen: {result1.get('message', '')} {result2.get('message', '')}"} 