from flask import Flask, request, jsonify
import time
import json

app = Flask(__name__)


@app.route('/gateway/consumerloan', methods=['GET', 'POST'])
def consumerloan():
    cook = request.cookies
    print(cook)
    if cook.__len__() > 0:
        return json.dumps({"Result": "ok", "Service": "consumerloan"})
    else:
        return json.dumps({"Result": "bad request, cookie required.", "Service": "consumerloan"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug = True)