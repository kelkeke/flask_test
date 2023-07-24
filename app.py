from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',  methods=['POST'])
def index():
    print("data: " + str(request.get_json()))
    print("source: " + str(request.remote_addr))
    print("source: " + str(request.environ['REMOTE_ADDR']))
    
    return "ok"
