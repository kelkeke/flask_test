from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/{}'.format(os.environ.get('SECRET')),  methods=['POST'])
def index():
    try:
        requests.post(os.environ.get('URL'), json=request.get_json(), verify=False)
    except:
        pass
    return "ok"
