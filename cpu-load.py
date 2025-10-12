import psutil
import time
while True:
	cpu_percent = psutil.cpu_percent(interval=1)
	print(f"cpu usage is : {cpu_percent}%")
	time.sleep(2)
