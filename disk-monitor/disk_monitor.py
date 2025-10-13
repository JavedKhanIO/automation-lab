import shutil
import time

#limit for warning
limit = 70
while True:
	total, used, free = shutil.disk_usage("/")
	percent_used = used / total * 100
	if percent_used > limit:
		print(f"Warning: disk usage is high:{percent_used:.2f}%")
	else:
		print(f"Disk usage: {percent_used:.2f}%")
	time.sleep(5)

