from flask import Flask, jsonify, request

app = Flask(__name__)

events = [
    {"id": 1, "name": "JFall", "date": "2024-10-30"},
    {"id": 2, "name": "DevCon", "date": "2024-11-30"}
]

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    if event:
        return jsonify(event)
    else:
        return jsonify({'message': 'Event not found'}), 404

@app.route('/events', methods=['POST'])
def create_event():
    new_event = request.get_json()
    events.append(new_event)
    return jsonify(new_event), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)