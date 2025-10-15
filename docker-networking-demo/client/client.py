import time
import requests

while True:
	try:
		response = requests.get("http://server:5000")
		print("Response from server :", response.text)
	except Exception as e:
		print("Server not reachable yet:", e)
	time.sleep(5)
