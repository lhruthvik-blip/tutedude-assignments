#!/usr/bin/python3

from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

app = Flask(__name__)

# MongoDB Atlas connection string (store in env variable for security)
load_dotenv()  # Load environment variables from .env file
mongo_uri = os.getenv('mongo_uri') or os.getenv('MONGO_URI')

try:
    client = MongoClient(mongo_uri, server_api=ServerApi('1'), retryWrites=True, w='majority', connectTimeoutMS=30000, socketTimeoutMS=30000)
    # Test connection
    client.admin.command('ping')
    print("Successfully connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    client = None

if client is not None:
    db = client.test
    collection = db["submissions"]
else:
    db = None
    collection = None


@app.route('/')
def homepage():
    return 'Hello from homepage!'


@app.route('/process', methods=['POST'])
def process():
    if collection is None:
        return jsonify(success=False, error="Database not connected")
    
    try:
        name = request.form.get('name')
        if not name:
            return jsonify(success=False, error="Name is required")

        # Insert into MongoDB
        collection.insert_one({"name": name})
        return jsonify(success=True, message=f"Hello, {name}!")
    except Exception as e:
        return jsonify(success=False, error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
