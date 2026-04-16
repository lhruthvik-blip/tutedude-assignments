#!/usr/bin/python3

from flask import Flask, render_template ,request
import os
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def homepage():
    day = datetime.now().today().strftime("%A")
    time = datetime.now().time().strftime("%H:%M:%S")
    #file_path = os.path.join(os.path.dirname(__file__), 'templates' , 'ex-index.html')
    return render_template('index.html', day=day, time=time)

@app.route('/next')
def next_page():
    return 'Hello from next page!' 

@app.route('/next/<variable>')
def getvariable(variable):
    return f'Hello from variable page after next page with variable: {variable}'

@app.route('/add/<a>/<b>')
def flaskadd(a, b):
    try:
        sum = int(a) + int(b)
        #return(f"sum = {sum}")
        #return("sum =" + str(sum))
        return f'The sum of {a} and {b} is: {sum}'  # sum is being returned as string, as integer type can not be returned.
    except ValueError:
        return 'Please provide valid integers for addition.'

@app.route('/api')
def nameage():
    name= request.values.get('name')
    age= request.values.get('age')

    result = {'name': name, 'age': age}
    #return f'Hello {name}, i see you are {age} years old.' # /api/?name=John&age=30
    return result  # this will return the result as a JSON response.



if __name__ == '__main__':
    app.run(debug=True)
