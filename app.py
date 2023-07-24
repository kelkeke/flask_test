from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',  methods=['POST'])
def index():
    print("data: " + request.get_json())
    print("source: " + request.remote_addr)
    print("source: " + request.environ['REMOTE_ADDR'])
    
    return "ok"
