import time, redis, json, requests

r = redis.Redis(host='redis', port=6379, decode_responses=True)
#setting upper limit for system values
CPU_THRESHOLD = 0.4
MEM_THRESHOLD = 13

#setting telegram bot
BOT_TOKEN = "8357532532:AAFny-e2Z_IVz5D8NnzWf5FAESCMrvkYdkU"
CHAT_ID = "8441690349"

while True:
	try:
		data = r.get("system_metrics")
		if data:
			metrics = json.loads(data)
			cpu = metrics["cpu"]
			mem = metrics["memory"]

			if cpu > CPU_THRESHOLD or mem > MEM_THRESHOLD:
				alert = f"ALERT!! CPU={cpu}%, Memory={mem}% at {metrics['timestamp']}"
				print(alert)
				r.publish("alerts", alert)

				#send telegram message
				message = f"Alert from smart monitor:\n{alert}"
				url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
				payload = {"chat_id": CHAT_ID, "text": message}
				try:
					response = requests.post(url, data=payload)
					if response.status_code != 200:
						print("Failed to send Telegram alert:", response.text)
				except Exception as te:
					print("Telegram send error:", te)
		time.sleep(5)
	except Exception as e:
		print(f"error reading metrics:", e)
		time.sleep(3)
