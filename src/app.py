# Import dependencies
from urllib import response
from flask import Flask, request, Response, jsonify
from flask_wtf.csrf import CSRFProtect
import json
# Set global app
app = Flask(__name__)

# Set security flask
csrf = CSRFProtect()
csrf.init_app(app)

# General data information (Hash)
"""
If you want to access data of topic, the complexity is O(1)
"""
temp_info = {
    "ping": ["pong"]
}
@app.route("/")
def index():
    return "Hello world"
@app.route("/message/<topic>", methods=["GET"])
def get_message(topic):
    if topic not in temp_info:
        return jsonify({"status": "fail"}), 400
    data = request.data
    return data, 200

@app.route("/message", methods=["POST"])
def post_message():
    if request.data:
        data = json.loads(request.data)
        message = data.get("message")
        topic = data.get("topic")
        if topic not in temp_info:
            temp_info[topic] = [message]
        else:
            temp_info[topic].append(message)
        return jsonify({"status": "ok"}), 200
    return jsonify({"status": "ok"}), 400
if __name__ == "__main__":
    app.run(port=8080, debug=True)