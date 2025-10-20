import time
import os
from datetime import datetime

LOG_DIR = "logs.txt"
os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(LOG_DIR, "app2.log")

while True:
	with open(log_file, "a") as f:
		f.write(f"[{datetime.now()}] App2: Everything looks fine. \n")
	print("App2 log written.")
	time.sleep(5)
