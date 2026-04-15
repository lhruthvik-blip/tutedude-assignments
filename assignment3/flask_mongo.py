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
db = client.test

collection = db['name_of_collection']

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('sign_up_index.html')


@app.route('/signup', methods=['POST'])
def submit_form():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return ("data entered succefully")  # Insert the form data into the MongoDB collection

@app.route('/view')
def view_data():
    data = list(collection.find())
    for item in data:
        del item['_id']  # Remove the '_id' field from the data
    
    data = {"data": data}
    return (data)


if __name__ == '__main__':
    app.run(debug=True)
