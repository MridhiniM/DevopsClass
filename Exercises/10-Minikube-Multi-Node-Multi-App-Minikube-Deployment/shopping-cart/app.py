from flask import Flask, jsonify, request

app = Flask(__name__)

cart = [
    {"product_id": 1, "name": "Laptop", "quantity": 1},
    {"product_id": 2, "name": "Headphones", "quantity": 2}
]

@app.route("/")
def home():
    return "Shopping Cart Service is running!"

@app.route("/cart")
def get_cart():
    return jsonify(cart)

@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    item = request.get_json()

    if not item or "product_id" not in item or "name" not in item:
        return jsonify({"error": "product_id and name are required"}), 400

    quantity = item.get("quantity", 1)

    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 1:
        return jsonify({"error": "quantity must be a positive integer"}), 400

    cart.append({
        "product_id": item["product_id"],
        "name": item["name"],
        "quantity": quantity
    })

    return jsonify({"message": "Item added", "cart": cart}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
