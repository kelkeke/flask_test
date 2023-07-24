from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/{}'.format(process.env.SECRET),  methods=['POST'])
def index():
    print("data: " + str(request.get_json()))
    
    request.post(process.env.URL, json=request.get_json())
    
    return "ok"
