#!/usr/bin/env python3

from flask import Flask, request
from pymongo import MongoClient, database

user_db_client = MongoClient("mongodb://mongo:27017/")
user_db = user_db_client.userdata
user_db_collection = user_db.records

app = Flask(__name__)

@app.route("/account", methods=['POST'])
def account():
    content = request.json
    if user_db_collection.find( { "name": content['name'] } ).count() > 0:
        return "Bad Request", 400
    else:
        user_db_collection.insert_one({"name": content['name']})
        return "Created", 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)