from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/")
def index():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["chads_test_database"]
    sunburst_collection = db["sunburst_collection"]
    with open("static/sunburst_data.json", "r") as file:
        print("Opening JSON file")
        data = json.load(file)
        print("JSON data loaded:")
    if isinstance(data, list):
        sunburst_collection.insert_many(data)
    else:
        sunburst_collection.insert_one(data)
    sunburst_cursor = sunburst_collection.find({}, {"_id": 0})
    sunburst_dict = [doc for doc in sunburst_cursor]
    sunburst_json_results = json.dumps(sunburst_dict)
    print("Sunburst JSON results", sunburst_json_results[0])
    client.close()
    return render_template("index.html", sunburst_data=sunburst_json_results)

    # return render_template(
    #     "index.html",
    #     sunburst_data=json.dumps(sunburst_json_results)
    #     .replace("\n", "\\n")
    #     .replace("\r", "\\r")
    #     .replace("'", "\\'"),
    # )


if __name__ == "__main__":
    app.run(debug=True)
