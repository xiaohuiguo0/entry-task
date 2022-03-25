from flask import  Flask, request, jsonify
import time

app = Flask(__name__)


@app.route('/gateway/risk', methods=['GET', 'POST'])
def risk():
    time.sleep(0.05)
    return jsonify( {"Result": "ok", "Service":"risk"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8003, debug = True)