from flask import  Flask, request, jsonify

app = Flask(__name__)


@app.route('/gateway/cashloan', methods=['GET', 'POST'])
def cashloan():
    return jsonify({"Result":"ok", "Service": "cashloan"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8002, debug = True)