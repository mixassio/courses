# -*- coding: utf-8 -*-

import random

from flask import Flask, request, jsonify


class Storage(object):  # storage = Storge()
    obj = None

    users = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.users = []
        return cls.obj

    def add(self, user):
        self.users.append(user)

    def get(self, index):
        return self.users[index]


class User(object):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_json(self):
        return {
            'username': self.username,
            'email': self.email,
        }


app = Flask(__name__, template_folder='templates')


@app.route('/user', methods=['GET', 'POST'])
def index():
    storage = Storage()

    if request.method == 'POST':
        data = request.get_json()

        user = User(data['username'], data['email'])
        storage.add(user)

        return jsonify({'status': 'done'})
    elif request.method == 'GET':
        data = [item.to_json() for item in storage.users]
        return jsonify(data)



if __name__ == '__main__':
    app.run(host='localhost', port=4000)
