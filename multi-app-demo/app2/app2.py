from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/result")
def get_result():
	try:
		response = requests.get("http://app1:5000/number")
		response.raise_for_status() #raises error if request fails
		data = response.json()
		number = data.get("number", 0)
		result = number * 2
		return jsonify({"original": number, "result": result})
	except Exception as e:
		return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
