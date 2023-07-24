from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/{}'.format(process.env.SECRET),  methods=['POST'])
def index():
    print("data: " + str(request.get_json()))
    
    requests.post(process.env.URL, json=request.get_json())
    
    return "ok"
