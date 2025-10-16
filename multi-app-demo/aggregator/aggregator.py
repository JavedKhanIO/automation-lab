import time
import requests

while True:
	try:
		response = requests.get("http://app2:5000/result")
		data = response.json()
		print(f"aggregator recieved: Original={data['original']}, Result={data['result']}")
	except Exception as e:
		print("error contacting app2:", e)
	time.sleep(5)
