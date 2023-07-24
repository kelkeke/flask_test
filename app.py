from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/{}'.format(os.environ.get['SECRET']),  methods=['POST'])
def index():
    print("data: " + str(request.get_json()))
    
    requests.post(os.environ.get['URL'], json=request.get_json())
    
    return "ok"
