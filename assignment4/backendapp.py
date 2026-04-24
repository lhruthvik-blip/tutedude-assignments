#!/usr/bin/python3

from flask import Flask, jsonify, render_template , request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import json


load_dotenv()  # Load environment variables from .env file
mongo_uri = os.getenv('mongo_uri')  # Get the MongoDB URI from environment variable
# Create a new client and connect to the server
client = MongoClient(mongo_uri, server_api=ServerApi('1'))
db = client.todo

collection = db['todo_collection'] 

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({"message": "Invalid or missing JSON"}), 400
        
        itemName = data.get("itemName")
        itemDescription = data.get("itemDescription")

        if not itemName or not itemDescription:
            return jsonify({"message": "Missing fields"}), 400

        collection.insert_one({
            "itemName": itemName,
            "itemDescription": itemDescription
        })

        return jsonify({"message": "Item saved successfully!"})
    
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
