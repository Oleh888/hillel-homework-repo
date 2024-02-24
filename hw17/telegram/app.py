import os
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"


@app.route("/alert", methods=["POST"])
def webhook():
    data = request.json

    for alert in data['alerts']:
        text = "⚠️ Alarm! \n" + "Level: " + alert['labels'].get('severity', '') + "\n" + alert['annotations']['description']
        payload = {"chat_id": CHAT_ID, "text": text}
        requests.post(TELEGRAM_URL, data=payload)
    return jsonify(status="success"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)
