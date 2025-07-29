from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = "EAAZAZADrR0r3cBPMk7WnCSKZButZCkBIWyqQgol5eOLX2rXZAgVSkLFrpdRLBqL7XaOJV0ZB8FUZAI4fKqb14u9vHksrlnbhZAHZCQrbk1wi8OZAllsAwxpnk4kkQqxGebwpE9HSfpsvrIT4QTuXEnlDqujhTTBZABNPJ98dqA1v0nPoQ7seqlZAwGRr3MiN7nCI8hydIdvySQZCGe7jHXEZBbXZAbPzbbZCi9iWTF4l6rbhnB4syMai3HBl9dd5QpdWtbiD6AZDZD"  # Set your token here

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        return "Invalid token", 403

    if request.method == "POST":
        data = request.json
        print("📩 Incoming Message:", data)
        return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
