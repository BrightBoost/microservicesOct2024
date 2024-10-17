from flask import Flask, jsonify, request
import os
import psycopg2

app = Flask(__name__)

DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'event_db')
DATABASE_USER = os.environ.get('DATABASE_USER', 'event_user')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'event_pass')

def get_connection():
    conn = psycopg2.connect(
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD
    )
    return conn

@app.route("/events", methods=["GET"])
def get_events():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM events;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    events = []
    for row in rows:
        events.append({'id': row[0], 'name':row[1], 'date':row[2]})
    
    return jsonify(events)

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    events = get_events()
    event = next((event for event in events if event['id'] == event_id), None)
    if event:
        return jsonify(event)
    else:
        return jsonify({'message': 'Event not found'}), 404

@app.route('/events', methods=['POST'])
def create_event():
    new_event = request.get_json()
    name = new_event.get('name')
    date = new_event.get('date')

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO events (name, date) VALUES (%s, %s) RETURNING id;', (name, date))
    event_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    new_event['id'] = event_id
    return jsonify(new_event), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)