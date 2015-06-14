#!/bin/python

# Dependencies:
# pip install flask
# pip install redis

from flask import Flask
from flask import request
import flask
import redis
import time
import json
from flask import Response, stream_with_context

app = Flask(__name__)
app.debug = True
db = redis.Redis('localhost') #connect to server

ttl = 31104000 #one year

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route('/', defaults={'path': ''}, methods = ['PUT', 'GET'])
@app.route('/<path:path>', methods = ['PUT', 'GET'])
def home(path):

    if (request.method == 'PUT'):
        event = request.json
        event['last_updated'] = int(time.time())
        event['ttl'] = ttl
        db.delete(path) #remove old keys
        db.hmset(path, event)
        db.expire(path, ttl)
        return json.dumps(event), 201

    if not db.exists(path):
        return "Error: thing doesn't exist"

    event = db.hgetall(path)
    event["ttl"] = db.ttl(path)
    #cast integers accordingly, nested arrays, dicts not supported for now  :(
    dict_with_ints = dict((k,int(v) if isInt(v) else v) for k,v in event.iteritems())
    return json.dumps(dict_with_ints), 200


if __name__ == "__main__":
    app.run()
