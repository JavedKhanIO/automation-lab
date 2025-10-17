import time
import requests

APP2_URL = "http://app2:5000/result"

def fetch_data():
	try:
		response = requests.get(APP2_URL, timeout=3)
		response.raise_for_status()
		data = response.json()
		print(f"[aggregator] recieved: Original={data.get('original')}, Result={data.get('result')}", flush=True)
	except Exception as e:
		print("[Aggregator] error contacting app2: {e}", flush=True)


if __name__ == "__main__":
	print("[Aggregator] service started. Polling app2 every 5 seconds...\n", flush=True)
	while True:
		fetch_data()
		time.sleep(5)
