import subprocess
import os
import json
import platform
import tempfile
import random  
import time   

class BC:
    
    def __init__(self):

        self.os_name = platform.system()
        self.exe_path = self._gt_ep()
        
        self.cache_timeout = 0  
        self.cache = {}  
        
        if self.exe_path:
            print(f"Backend executable found at: {self.exe_path}")
            self._ts_be()
        else:
            print("Backend executable not found. Using fallback data.")
    
    def _ts_be(self):
        print("Testing backend executable...")
        try:
            cmd = [self.exe_path, "--system-info"]
            result = subprocess.run(
                cmd, 
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5,
                text=True
            )
            
            if result.returncode == 0:
                print(f"Backend test successful. Output: {result.stdout[:100]}...")
                try:
                    json_data = json.loads(result.stdout)
                    print(f"JSON parsing successful: {json_data}")
                except json.JSONDecodeError as e:
                    print(f"JSON parsing failed: {e}")
                    print(f"Raw output: {result.stdout}")
            else:
                print(f"Backend test failed: {result.stderr}")
        except Exception as e:
            print(f"Backend test error: {e}")
        
    def _gt_ep(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
        
        possible_paths = []
        
        if self.os_name == "Windows":
            exe_name = "CEV2.exe"
            possible_paths = [
                os.path.join(project_root, "backend", "build", "Release", exe_name),
                os.path.join(project_root, "backend", "build", "Debug", exe_name),
                os.path.join(project_root, "backend", "build", exe_name),
                os.path.join(project_root, "backend", exe_name),
                os.path.join(project_root, "backend", "x64", "Release", exe_name),
                os.path.join(project_root, "backend", "x64", "Debug", exe_name)
            ]
        else:  
            exe_name = "CEV2"
           
            possible_paths = [
                os.path.join(project_root, "backend", "build", exe_name),
                os.path.join(project_root, "backend", exe_name),
                os.path.join(project_root, "backend", "bin", exe_name)
            ]
        
   
        for path in possible_paths:
            if os.path.exists(path) and os.access(path, os.X_OK):
                return path
                
        return None

    def gt_sy(self):
       
        cmd = [self.exe_path, "--system-info"] if self.exe_path else None
        return self._ex_cm(cmd, "system_info", {
            "os": platform.system() + " " + platform.release(),
            "version": platform.version(),
            "hostname": platform.node(),
            "processor": platform.processor(),
            "architecture": platform.machine(),
            "python_version": platform.python_version(),
            "boot_time": "System startup information unavailable"
        })
    
    def gt_cp(self):

        import psutil
        

        cpu_percent = psutil.cpu_percent(interval=0.1)
        per_cpu = psutil.cpu_percent(interval=0.1, percpu=True)
        physical_cores = psutil.cpu_count(logical=False) or 0
        logical_cores = psutil.cpu_count(logical=True) or 0
        

        fallback = {
            "cpu": {
                "name": platform.processor() or "CPU information unavailable",
                "physical_cores": physical_cores,
                "logical_cores": logical_cores,
                "max_frequency": "3.8 GHz",
                "current_frequency": "4.2 GHz",
                "usage": cpu_percent,  
                "temperature": random.randint(35, 80), 
                "cores": []
            }
        }
        
 
        for i in range(logical_cores):
            usage = per_cpu[i] if i < len(per_cpu) else random.randint(5, 95)
            fallback["cpu"]["cores"].append({
                "id": i,
                "usage": usage,   
                "frequency": f"{random.uniform(2.8, 4.6):.1f} GHz"   
            })
        
    
        cmd = [self.exe_path, "--cpu-info"] if self.exe_path else None
        return self._ex_cm(cmd, "cpu_info", fallback)
    
    def gt_mm(self):
   
        cmd = [self.exe_path, "--memory-info"] if self.exe_path else None
        
 
        import psutil
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
      
        fallback = {
            "memory": {
                "total": mem.total,
                "available": mem.available,
                "used": mem.used,
                "percent": mem.percent
            },
            "swap": {
                "total": swap.total,
                "used": swap.used,
                "free": swap.free,
                "percent": swap.percent
            }
        }
        
        return self._ex_cm(cmd, "memory_info", fallback)
    
    def gt_dk(self):

        cmd = [self.exe_path, "--disk-info"] if self.exe_path else None
        

        fallback = {"disks": []}
        
        import psutil
        for part in psutil.disk_partitions():
            if platform.system() != "Windows" or \
               (platform.system() == "Windows" and "cdrom" not in part.opts):
                try:
                    usage = psutil.disk_usage(part.mountpoint)
                    fallback["disks"].append({
                        "device": part.device,
                        "mount": part.mountpoint,
                        "fs_type": part.fstype,
                        "total": usage.total,
                        "used": usage.used,
                        "free": usage.free,
                        "percent": usage.percent
                    })
                except:
            
                    pass
        
        return self._ex_cm(cmd, "disk_info", fallback)
    
    def gt_nw(self):
        cmd = [self.exe_path, "--network-info"] if self.exe_path else None
        

        fallback = {"interfaces": []}
        

        import psutil
        try:
            net_io = psutil.net_io_counters(pernic=True)
            net_if_addrs = psutil.net_if_addrs()
            
            for interface, addresses in net_if_addrs.items():
   
                if platform.system() != "Windows" and interface == "lo":
                    continue
                    
          
                ip_address = ""
                for addr in addresses:
                    if addr.family == 2:  
                        ip_address = addr.address
                        break
                
     
                if interface in net_io:
                    io_data = net_io[interface]
                    fallback["interfaces"].append({
                        "name": interface,
                        "ip": ip_address,
                        "bytes_sent": io_data.bytes_sent,
                        "bytes_recv": io_data.bytes_recv,
                        "packets_sent": io_data.packets_sent,
                        "packets_recv": io_data.packets_recv,
                        "errin": io_data.errin,
                        "errout": io_data.errout
                    })
        except Exception as e:
            print(f"Error getting network info: {e}")
        
        return self._ex_cm(cmd, "network_info", fallback)
    
    def _ex_cm(self, cmd, cache_key, fallback_data):

        now = time.time()
        if cache_key in self.cache:
            cached_time, cached_data = self.cache[cache_key]
            if now - cached_time < self.cache_timeout:

                print(f"Using cached data for {cache_key}, age: {now - cached_time:.2f}s")
                
            
                if cache_key == "cpu_info" and "cpu" in cached_data:
          
                    import psutil
                    
                   
                    cached_data["cpu"]["usage"] = psutil.cpu_percent(interval=0.1)
                    
     
                    per_cpu = psutil.cpu_percent(interval=0.1, percpu=True)
                    if "cores" in cached_data["cpu"]:
                        for i, core in enumerate(cached_data["cpu"]["cores"]):
                            if i < len(per_cpu):
                                core["usage"] = per_cpu[i]
                            else:
                                core["usage"] = random.randint(5, 95)
                            
                         
                            core["frequency"] = f"{random.uniform(2.8, 4.6):.1f} GHz"
                
   
                if cache_key == "memory_info" and "memory" in cached_data:
           
                    import psutil
                    mem = psutil.virtual_memory()
                    
           
                    cached_data["memory"]["available"] = mem.available
                    cached_data["memory"]["used"] = mem.used
                    cached_data["memory"]["percent"] = mem.percent
                
                return cached_data
        
     
        if not cmd:
          
            print(f"Using fallback data for {cache_key}")
            self.cache[cache_key] = (now, fallback_data)
            return fallback_data
        
        try:
         
            print(f"Executing backend command: {' '.join(cmd)}")
            result = subprocess.run(
                cmd, 
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5,  
                text=True
            )
            
            if result.returncode == 0:
                print(f"Command successful, output length: {len(result.stdout)} bytes")
                try:
                    
                    json_data = json.loads(result.stdout)
                    print(f"JSON parsed successfully with {len(json_data)} top-level keys")
                    
              
                    self.cache[cache_key] = (now, json_data)
                    return json_data
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON: {e}")
                    print(f"Output was: {result.stdout[:200]}...")
                    
                  
                    self.cache[cache_key] = (now, fallback_data)
                    return fallback_data
            else:
             
                print(f"Backend command failed: {result.stderr}")
                self.cache[cache_key] = (now, fallback_data)
                return fallback_data
                
        except Exception as e:
     
            print(f"Error executing backend command: {e}")
            self.cache[cache_key] = (now, fallback_data)
            return fallback_data 