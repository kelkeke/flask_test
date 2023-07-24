from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/{}'.format(secret),  methods=['POST'])
def index():
    print("data: " + str(request.get_json()))
    
    request.post(process.env.URL, json=request.get_json())
    
    return "ok"
