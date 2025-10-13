import requests
import time

LOG_FILE = "uptime_log.txt"
URL = "https://www.google.com"

while True:
	try:
		response = requests.get(URL,timeout=5)
		status = "UP" if response.status_code == 200 else f"DOWN ({response.status.code})"
	except requests.requestsException:
		status = "DOWN (no response)"
	with open(LOG_FILE, "a") as f:
		f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {URL} is {status}\n")
	print(f"{URL} is {status}")
	time.sleep(5)

