from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 75000},
    {"id": 2, "name": "Headphones", "price": 2500},
    {"id": 3, "name": "Keyboard", "price": 1500}
]

@app.route("/")
def home():
    return "Product Catalog Service is running!"

@app.route("/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
