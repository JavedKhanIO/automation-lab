import psutil
import time
from datetime import datetime


LOG_FILE = "system_monitor.txt" #to log details

def log_system_usage():
	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	cpu = psutil.cpu_percent(interval=1)
	memory = psutil.virtual_memory().percent
	disk = psutil.disk_usage('/').percent
	log_line = f"{now} | CPU:{cpu}% | Memory:{memory}% | Disk:{disk}%"
#defininf log fie
	with open(LOG_FILE, "a") as f:
		f.write(log_line + "\n")
	print(log_line) #printing on console

if __name__ == "__main__":
	print("system monitor started. Logging every 5 seconds ")

	while True:
		log_system_usage()
		time.sleep(5)
	
