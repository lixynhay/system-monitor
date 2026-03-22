import psutil
import time
import os
import platform
from datetime import datetime

class SystemCore:
    _prev_net = psutil.net_io_counters()
    _prev_time = time.time()
    psutil.cpu_percent(interval=None)

    @staticmethod
    def get_metrics():
        # Network speed calculation logic
        current_net = psutil.net_io_counters()
        current_time = time.time()
        dt = current_time - SystemCore._prev_time
        if dt <= 0: dt = 1

        up_speed = (current_net.bytes_sent - SystemCore._prev_net.bytes_sent) / dt / (1024**2)
        down_speed = (current_net.bytes_recv - SystemCore._prev_net.bytes_recv) / dt / (1024**2)
        
        SystemCore._prev_net = current_net
        SystemCore._prev_time = current_time

        # Hardware sensors data (Root required for temp)
        temp = "N/A"
        try:
            for i in range(10):
                path = f"/sys/class/thermal/thermal_zone{i}/temp"
                if os.path.exists(path):
                    with open(path, 'r') as f:
                        temp = f"{int(f.read().strip()) / 1000:.1f}°C"
                        break
        except: pass

        return {
            "sys": {
                "os": f"{platform.system()} {platform.release()}",
                "uptime": str(datetime.now() - datetime.fromtimestamp(psutil.boot_time())).split('.')[0],
                "cpu_temp": temp,
                "is_root": os.getuid() == 0
            },
            "stats": {
                "cpu": psutil.cpu_percent(interval=None),
                "ram": psutil.virtual_memory().percent,
                "disk": psutil.disk_usage('/').percent,
                "net_down": f"{down_speed:.2f}",
                "net_up": f"{up_speed:.2f}"
            },
            "procs": [
                {"pid": p.info['pid'], "name": p.info['name'][:15], "cpu": p.info['cpu_percent']}
                for p in sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), 
                         key=lambda x: x.info['cpu_percent'] or 0, reverse=True)[:5]
            ],
            "logs": SystemCore.get_last_logs()
        }

    @staticmethod
    def get_last_logs():
        # System log tailing (Root recommended)
        try:
            return os.popen('dmesg | tail -n 5').read().splitlines()
        except:
            return ["Logs unavailable"]

    @staticmethod
    def kill_process(pid: int):
        # Process management
        try:
            os.kill(pid, 9)
            return True
        except:
            return False
