import requests,time
from flask import Flask, jsonify
app = Flask(__name__)
URL_TO_CHECK = ["https://www.google.com", "https://www.github.com"]

@app.route('/status')

def check_url():
	results = []
	for url in URL_TO_CHECK:
		try:
			start = time.time()
			resp = requests.get(url, timeout=5)
			latency = time.time() - start
			results.append({
				"url": url,
				"status": resp.status_code,
				"latency": round(latency, 2),
				"up": resp.status_code == 200
			})

		except:
			results.append({"url": url, "error": "failed"})
	return jsonify(results)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port= 5000)
