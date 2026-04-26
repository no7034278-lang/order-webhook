from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route("/webhook/order", methods=["POST"])
def order():
    data = request.json
    print("Order received:", data)

    orders.append(data)
    return jsonify({"status": "ok"}), 200


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run()