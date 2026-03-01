import psutil
import datetime

# Get system stats
cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

# Get uptime
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
uptime = datetime.datetime.now() - boot_time

# Format report
report = f"""
===== SERVER HEALTH REPORT =====
Time: {datetime.datetime.now()}

CPU Usage: {cpu_usage}%
Memory Usage: {memory.percent}%
Disk Usage: {disk.percent}%

System Uptime: {uptime}
"""

print(report)

# Save to log file
with open("health_report.log", "a") as file:
    file.write(report)
