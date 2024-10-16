from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

EVENT_SERVICE_URL = os.environ.get('EVENT_SERVICE_URL', 'http://event_service:5002')

users = [
    {'id': 1, 'name': 'maaike', 'email': 'maaike@example.com'},
    {'id': 2, 'name': 'adnane', 'email': 'adnane@example.com'}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>/events', methods=['GET'])
def get_user_events(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        # Fetch events from Event Service
        response = requests.get(f'{EVENT_SERVICE_URL}/events')
        if response.status_code == 200:
            events = response.json()
            return jsonify({'user': user, 'events': events})
        else:
            return jsonify({'message': 'Failed to fetch events'}), response.status_code
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)