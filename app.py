from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid


app = Flask(__name__)


# @app.route("/")
# def index():
#     client = MongoClient("mongodb://localhost:27017/")
#     db = client["chads_test_database"]

#     collection_name = "sunburst_collection"
#     print(f"Collection name: {collection_name}")
#     # Check if the collection already exists
#     if collection_name not in db.list_collection_names():
#         # Create the collection if it doesn't exist
#         try:
#             db.create_collection(collection_name)
#         except CollectionInvalid:
#             print(f"Collection '{collection_name}' already exists.")

#         sunburst_collection = db[collection_name]

#         with open("/static/sunburst_data.json", "r") as file:
#             print("Opening JSON file")
#             data = json.load(file)
#             print("JSON data loaded:")

#         if isinstance(data, list):
#             sunburst_collection.insert_many(data)
#         else:
#             sunburst_collection.insert_one(data)
#     else:
#         sunburst_collection = db[collection_name]


#     sunburst_cursor = sunburst_collection.find({}, {"_id": 0})
#     sunburst_list = [doc for doc in sunburst_cursor]
#     sunburst_json_results = json.dumps(sunburst_list)
#     print("Sunburst JSON results", sunburst_json_results)
#     client.close()
#     return render_template("index.html", sunburst_data=sunburst_json_results)
@app.route("/")
def index():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["chads_test_database"]
    sunburst_collection = db["sunburst_collection"]
    sunburst_collection.drop()  # Drop the existing collection

    with open("static/sunburst_data.json", "r") as file:
        print("Opening JSON file")
        data = json.load(file)
        print("JSON data loaded:")

    if isinstance(data, list):
        sunburst_collection.insert_many(data)
    else:
        sunburst_collection.insert_one(data)

    sunburst_collection = db["sunburst_collection"]  # Create the collection again
    sunburst_cursor = sunburst_collection.find({}, {"_id": 0})
    sunburst_list = [doc for doc in sunburst_cursor]
    sunburst_json_results = json.dumps(sunburst_list)
    print("Sunburst JSON results", sunburst_json_results[0])
    client.close()
    return render_template("index.html", sunburst_data=sunburst_json_results)


if __name__ == "__main__":
    app.run(debug=True)
