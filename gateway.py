from flask import Flask, request, jsonify
import requests
import json

app=Flask(__name__)

@app.route('/gateway', methods=['GET', 'POST'])
def gateway():
    url='http://127.0.0.1:'
    try:
        consumerloan_1 = req(url, '8001', '/gateway/consumerloan').content.decode('utf-8')
        caskloan_1 = req(url, '8002', '/gateway/cashloan').content.decode('utf-8')
        risk_1 = req(url, '8003', '/gateway/risk').content.decode('utf-8')
        try:
            consumerloan_ = json.loads(req(url, '8001', '/gateway/consumerloan').content.decode('utf-8'))
            caskloan_ = json.loads(req(url, '8002', '/gateway/cashloan').content.decode('utf-8'))
            risk_ = json.loads(req(url, '8003', '/gateway/risk').content.decode('utf-8'))
            return jsonify({"Code": "200", "Result": "ok"})
        except:
            return jsonify({"Code": "500", "Result": "Gateway内部异常"})
    except:
        return jsonify({"Code": "501", "Result": "Gateway可用，下游服务不可用"})



def req(url, port, para):
    return requests.post(url+port+para)

app.run(host="127.0.0.1", port=8000, debug = True)