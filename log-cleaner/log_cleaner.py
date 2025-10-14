import os
import time
import sys
from datetime import datetime, timedelta

#specify folder to clean

CLEAN_FOLDER = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/devops-projects/log-cleaner/logs")

DAYS_OLD = 7 #days old file to delete

def delete_old_files():
	now = datetime.now()
	cutoff = now - timedelta(days=DAYS_OLD)
	
	#creatig folder if doesnt exists
	os.makedirs(CLEAN_FOLDER, exist_ok=True)

	for filename in os.listdir(CLEAN_FOLDER):
		file_path = os.path.join(CLEAN_FOLDER, filename)
		if os.path.isfile(file_path):
			file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
			if file_mtime < cutoff:
				os.remove(file_path)
				print(f"[{datetime.nowa().strftime('%Y-%m-%d %H:%M%S')}] Deleted: {filename}")
if __name__ == "__main__":
	print(f"Log Cleaner started, cleaning '{CLEAN_FOLDER}' for files older than {DAYS_OLD} days,")

	while True:
		delete_old_files()
		time.sleep(60)
