from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    print('data recieved')
    return "ok"
