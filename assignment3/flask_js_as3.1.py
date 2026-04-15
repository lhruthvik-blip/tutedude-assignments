#!/usr/bin/python3

from flask import Flask, jsonify
import json
import os

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Hello from homepage!' 

@app.route('/api', methods=['GET'])
def get_data():
    # Read data from backend file
    file_path = os.path.join(os.path.dirname(__file__), 'templates' , 'data.json') # getting the absolute path of a file. now the app can be run from any directory and still will be able to access the json file.
    with open(file_path, 'r') as f: # use this if json file is in a different folder("templates")
    #with open('data.json', 'r') as f:
        data = json.load(f)
    # Return as JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
