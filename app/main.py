from flask import Flask, render_template
import os

app = Flask(__name__)
API_KEY = os.environ.get('API_KEY')

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to CodingX "+API_KEY+"</h1>"
