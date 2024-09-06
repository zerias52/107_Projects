from flask import Flask, request, jsonify
from config import db

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask!"

@app.get("/about")
def about():
    me = {"name": "Brett Byrd"}
    return jsonify(me)

@app.get("/footer")
def footer():
    page_name = {"pageName": "organika"}
    return jsonify(page_name)

# Define products as a global variable
products = []

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/products")
def get_products():
    return jsonify(products)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    db.products.insert_one(item)
    products.append(item)
    return jsonify(fix_id(item)), 201

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_item = request.get_json()
    if 0<=index<len(products):
        products[index] = updated_item
        return jsonify(updated_item), 201
    else:
        return "That index does not exist."

if __name__ == "__main__":
    app.run(debug=True)