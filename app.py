from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

def load_licenses():
    with open("licenses.json", "r") as f:
        return json.load(f)

def save_licenses(data):
    with open("licenses.json", "w") as f:
        json.dump(data, f)

@app.route("/")
def index():
    return "Kaka Ali License API is running."

@app.route("/check", methods=["POST"])
def check_license():
    data = request.json
    code = data.get("license")
    today = datetime.today().strftime("%Y-%m-%d")

    licenses = load_licenses()
    if code in licenses:
        exp_date = licenses[code]["expires"]
        if exp_date >= today:
            return jsonify({"status": "valid", "expires": exp_date})
        else:
            return jsonify({"status": "expired", "expires": exp_date})
    return jsonify({"status": "invalid"})

if __name__ == "__main__":
    app.run()
