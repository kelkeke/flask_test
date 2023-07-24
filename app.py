from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',  methods=['POST'])
def index():
    print("data: " + str(request.get_json()))
    print("headers: " + str(request.headers))
    
    return "ok"
