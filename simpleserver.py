#!/usr/bin/env python
# coding: utf-8
import sys
print(sys.version)

# Creat a Blockchain
# Needed packages:
# - flask==0.12.2
# - Postman HTTP Client: 

#import libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/req_status', methods = ['GET'])
def req_status():
    response = {'message': 'the status of your request is...'}
    return jsonify(response), 200


#Running the app
# main driver function
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)

