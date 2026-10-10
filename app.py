from datetime import datetime

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/hello", methods=["POST"])
def hello():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "friend").strip() or "friend"
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    return jsonify(
        {
            "message": f"{greeting}, {name}! Welcome to ASTRA.",
            "serverTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )


@app.route("/api/status")
def status():
    return jsonify({"ok": True, "app": "ASTRA", "stack": "HTML, CSS, JS, Python"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
