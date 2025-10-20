import psutil
from datetime import datetime
import time

LOG_FILE = "log.txt"

def system():
	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	cpu = psutil.cpu_percent(interval=1)
	disk = psutil.disk_usage('/').percent
	memory = psutil.virtual_memory().percent
	log_line = f"{now} | cpu:{cpu} | disk: {disk} | memory:{memory}"

	with open(LOG_FILE, "a") as f:
		f.write(log_line + "\n")
	print(log_line)
	if cpu > 0.3:
		print("overusing cpu load")

if __name__ == "__main__":
	print("now loging system usage")
	while True:
		system()
		time.sleep(5)
