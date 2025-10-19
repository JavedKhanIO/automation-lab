import time
import requests

while True:
	try:
		r=requests.get("http://hello:5500/hello")
		print("getting response from server: ", r.text)
		with open("log.txt", "a") as f:
			timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
			f.write(f"[{timestamp}] {r.text}\n")
	except Exception as e:
		print("error getting the response", e)
	time.sleep(5)
