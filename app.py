from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',  methods=['POST'])
def index():
    print(request.get_json())
    return "ok"
