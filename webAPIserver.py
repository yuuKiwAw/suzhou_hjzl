# Author : Yuki
# python 3.8
# coding=utf-8
import flask
import json
from gevent import pywsgi

app = flask.Flask(__name__)
# app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False


def weatherINFOjson():
    with open('./json/weatherINFO.json', 'r', encoding='utf-8') as f:
        result = json.load(f)
        return result


@app.route('/hjzlAQI', methods=['GET'])
def home():
    return weatherINFOjson()


server = pywsgi.WSGIServer(('192.168.123.8', 8090), app)
server.serve_forever()
