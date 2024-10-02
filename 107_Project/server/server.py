from flask import Flask, request, jsonify
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # warning, this disables CORS policy

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
def read_products():
    cursor = db.catalog.find({})
    catalog = []
    for prod in cursor:
        catalog.append(fix_id(prod))
    return jsonify(catalog)


@app.post("/api/products")
def save_products():
    item = request.get_json()
    db.catalog.insert_one(item)
    return jsonify(fix_id(item)), 201


@app.get("/api/coupons")
def read_coupons():
    cursor = db.coupons.find({})
    coupons = []
    for coupon in cursor:
        coupons.append(fix_id(coupon))
    return jsonify(coupons)


@app.post("/api/coupons")
def save_coupons():
    item = request.get_json()
    db.coupons.insert_one(item)
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