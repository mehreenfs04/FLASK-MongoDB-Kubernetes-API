## GET
import os  
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask + MongoDB app is running on Kubernetes"


"""
MONGO_URI = os.environ.get(
    "MONGO_URI", 
    "mongodb://admin:admin@mongodb-service:27017/BOOKSTORE?authSource=admin"
)
"""

client = MongoClient(
    os.environ.get(
        "MONGO_URI",
        "mongodb://localhost:27017/BOOKSTORE"
    )
)

database = client["BOOKSTORE"]
books_collection = database["books"]

database = client["BOOKSTORE"]  
books_collection = database["books"]


@app.route("/books", methods=["GET"])
def get_books():
    books = []
    for book in books_collection.find():
        book["_id"] = str(book["_id"])
        books.append(book)
    return jsonify(books)



## CREATE (POST)

@app.route("/books", methods=["POST"])
def insert_book():
    data = request.get_json()

    new_book = {
        "title": data.get("title"),
        "author": data.get("author"),
        "price": data.get("price")
    }

    outcome = books_collection.insert_one(new_book)

    return jsonify({
        "message": "Book added",
        "id": str(outcome.inserted_id)
    }), 201


## READ BY ID

@app.route("/books/<id>", methods=["GET"])
def retrieve_book(id):
    book = books_collection.find_one({"_id": ObjectId(id)})

    if not book:
        return jsonify({"error": "Book not found!"}), 404

    book["_id"] = str(book["_id"])
    return jsonify(book)



## UPDATE

@app.route("/books/<id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()

    update_data = {
        "title": data.get("title"),
        "author": data.get("author"),
        "price": data.get("price")
    }

    result = books_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Book not found!"}), 404

    return jsonify({"message": "Book has been updated successfully"})



## DELETE

@app.route("/books/<id>", methods=["DELETE"])
def delete_book(id):
    result = books_collection.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        return jsonify({"error": "Book not found!"}), 404

    return jsonify({"message": "Book deleted successfully"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)