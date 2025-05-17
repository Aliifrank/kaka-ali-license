from flask import Flask, request, jsonify

app = Flask(__name__)

licenses = {
    "abc123": "2025-12-01",
    "def456": "2025-06-30"
}

@app.route("/check", methods=["GET"])
def check():
    code = request.args.get("code")
    if code in licenses:
        return jsonify({"status": "valid", "expire_date": licenses[code]})
    else:
        return jsonify({"status": "invalid"}), 404

if __name__ == "__main__":
    app.run(debug=True)
