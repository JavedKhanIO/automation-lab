import socket, time, os, psutil, flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify({
		"message": "System info API v1.0",
		"endpoints": ["/", "/health", "/system"]
	})

@app.route('/health')
def health():
	return jsonify({
		"status": "healthy",
		"timestamp": time.time()
	})

@app.route('/system')
def system_info():
	hostname = socket.gethostname()
	uptime = time.time() - psutil.boot_time()
	memory = psutil.virtual_memory()

	return jsonify({
		"hostname":hostname,
		"timestamp": time.time(),
		"uptime_seconds": round(uptime, 2),
		"memory_usage_percent": memory.percent,
		"memory_available": round(memory.available / (1024**3), 2),
		"container_id": os.getenv("HOSTNAME", "localhost")
	})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
