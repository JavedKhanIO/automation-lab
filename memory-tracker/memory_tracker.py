import psutil
import time

LOG_FILE = "memory_log.txt"
while True:
	memory = psutil.virtual_memory()
	with open(LOG_FILE, "a") as f:
		f.write(f"Used: {memory.percent}% | Available : {memory.available / (1024**2):.2f}MB\n")
	print(f"memory usage logged: {memory.percent}%")
	time.sleep(5)
