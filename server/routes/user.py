from flask import Flask
from app import app

@app.route('/user/', methods=['GET'])
def hello_user():
    return "User Hello"