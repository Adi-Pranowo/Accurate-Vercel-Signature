from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def signature():
    return jsonify({"debug": "OK"})

app = app