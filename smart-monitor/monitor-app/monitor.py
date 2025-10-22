import time, redis, json, psutil
from datetime import datetime
#introducing  redis to transport info between apps
r = redis.Redis(host='redis', port=6379, decode_responses=True)

while True:
	metrics = {
		"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
		"cpu": psutil.cpu_percent(interval=1),
		"memory": psutil.virtual_memory().percent
	}
	r.set("system_metrics", json.dumps(metrics))
	print("published:", metrics)
	time.sleep(5)
