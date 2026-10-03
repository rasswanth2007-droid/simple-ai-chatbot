import json
import random
from flask import Flask, request, jsonify, send_file

# Load chatbot data from JSON file
with open("responses.json", "r") as file:
    chatbot = json.load(file)

app = Flask(__name__)


@app.route("/")
def index():
    return send_file("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data.get("message", "").lower().strip()

    found = False
    reply = ""

    # Check each condition
    for key, entry in chatbot.items():
        if key == "default":
            continue

        for condition in entry["conditions"]:
            if condition in user:
                reply = random.choice(entry["responses"])
                found = True
                break

        if found:
            break

    # Default response
    if not found:
        reply = random.choice(chatbot["default"]["responses"])

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)