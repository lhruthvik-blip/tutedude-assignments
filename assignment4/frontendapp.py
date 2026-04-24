#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('todo.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        itemName = request.form['itemName']
        itemDescription = request.form['itemDescription']

        response = requests.post("http://localhost:5000/submittodoitem", json={
            "itemName": itemName,
            "itemDescription": itemDescription
        })
        
        return f"Response from backend: {response.json().get('message')}"
    
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(port=3000, debug=True)
