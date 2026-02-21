import redis, logging, os
from logging.handlers import RotatingFileHandler

r = redis.Redis(host='redis', port=6379, decode_responses=True)

#using loggin handler to log values.
os.makedirs("/app/logs", exist_ok=True)
logger = logging.getLogger("SmartMonitor")
handler = RotatingFileHandler("logs/log.txt", maxBytes=100*1024, backupCount=1)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

pubsub = r.pubsub()
pubsub.subscribe("alerts")

print("Aggregator started, waiting for alerts...")

for message in pubsub.listen():
	if message['type'] == 'message':
		alert = message['data']
		print(alert)
		logger.info(alert)
