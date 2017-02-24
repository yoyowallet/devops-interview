#!/usr/bin/env python
import json
import os

import datetime
import jwt
from flask import Flask, jsonify
from flask import current_app
from flask import request

app = Flask(__name__)

# In-memory user database
with open(os.path.join(os.path.dirname(__file__), 'users.json'), 'rb') as f:
    users = json.load(f)


@app.route('/token', methods=['POST'])
def create_token():
    """
    Authenticates a user by username and password, returning an authentication token (valid for 30s)
    that can be used to make authenticated requests to other microservices.
    """
    username: str = request.form.get('username')
    password: str = request.form.get('password')

    if not username:
        return jsonify(error='Username is blank'), 422
    if not password:
        return jsonify(error='Password is blank'), 422

    for user in users:
        # Find user by username
        if user['username'] == username:
            # Validate password
            if user['password'] == password:
                payload = {
                    'user_id': user['id'],
                    'username': user['username'],
                    'can_transact': user['can_transact'],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30),  # jwt expiration time claim
                }

                token = jwt.encode(
                    payload,
                    current_app.config['JWT_SECRET'],
                    algorithm='HS256',
                )

                return jsonify(token=token.decode('utf-8'))
            else:
                return jsonify(error='Invalid password'), 401
    else:
        return jsonify(error='User not found'), 404


@app.route('/health')
def health():
    return jsonify(healthy=True)


if __name__ == '__main__':
    # Env
    http_port: int = int(os.getenv('HTTP_PORT', 5000))
    jwt_secret: str = os.environ['JWT_SECRET']

    # Flask config
    app.config['JWT_SECRET'] = jwt_secret

    # Run app
    app.run(host='0.0.0.0', port=http_port, threaded=True)
