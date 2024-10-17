### **Exercise 2: Connect Microservices to the Databases**

*Duration: Approximately 60 minutes*

**What you'll get out of this exercise:**

- Learn how to connect Python microservices to PostgreSQL databases running in Docker containers.
- Implement CRUD (Create, Read, Update, Delete) operations in your microservices to interact with the databases.
- Understand how to use environment variables for database configuration.

---

#### **Instructions Part 1: Update Event Service to Use the Database**

**0. Update and restart Docker compose**

```yaml
  services:
    event_db:
      image: postgres:13
      environment:
        - POSTGRES_USER=event_user
        - POSTGRES_PASSWORD=event_pass
        - POSTGRES_DB=event_db
      volumes:
        - event_db_data:/var/lib/postgresql/data
      networks:
        - eventhive-network

    user_db:
      image: postgres:13
      environment:
        - POSTGRES_USER=user_user
        - POSTGRES_PASSWORD=user_pass
        - POSTGRES_DB=user_db
      volumes:
        - user_db_data:/var/lib/postgresql/data
      networks:
        - eventhive-network

    event_service:
      build: ./event_service
      ports:
        - "5000:5000"
      environment:
        - DATABASE_HOST=event_db
        - DATABASE_PORT=5432
        - DATABASE_NAME=event_db
        - DATABASE_USER=event_user
        - DATABASE_PASSWORD=event_pass
      depends_on:
        - event_db
      networks:
        - eventhive-network

    user_service:
      build: ./user_service
      ports:
        - "5001:5001"
      environment:
        - DATABASE_HOST=user_db
        - DATABASE_PORT=5432
        - DATABASE_NAME=user_db
        - DATABASE_USER=user_user
        - DATABASE_PASSWORD=user_pass
      depends_on:
        - user_db
      networks:
        - eventhive-network

  volumes:
    event_db_data:
    user_db_data:

  networks:
    eventhive-network:
      driver: bridge

```

**1. Install Database Dependencies in Event Service:**

- Navigate to the `event_service` directory:

  ```bash
  cd event_service
  ```

- Activate the virtual environment:

  ```bash
  source venv/bin/activate
  ```

- Install `psycopg2-binary` for PostgreSQL connectivity:

  ```bash
  pip install psycopg2-binary
  ```

- Update `requirements.txt` (if you have one):

  ```bash
  echo "psycopg2-binary" >> requirements.txt
  ```

**2. Modify `app.py` to Connect to PostgreSQL:**

- Import `psycopg2` and update your imports:

  ```python
  import os
  import psycopg2
  from flask import Flask, jsonify, request
  ```

- Set up the database connection parameters using environment variables:

  ```python
  DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
  DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
  DATABASE_NAME = os.environ.get('DATABASE_NAME', 'event_db')
  DATABASE_USER = os.environ.get('DATABASE_USER', 'event_user')
  DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'event_pass')
  ```

- Create a function to get a database connection:

  ```python
  def get_db_connection():
      conn = psycopg2.connect(
          host=DATABASE_HOST,
          port=DATABASE_PORT,
          database=DATABASE_NAME,
          user=DATABASE_USER,
          password=DATABASE_PASSWORD
      )
      return conn
  ```

- Update the `/events` route to fetch data from the database:

  ```python
  @app.route('/events', methods=['GET'])
  def get_events():
      conn = get_db_connection()
      cur = conn.cursor()
      cur.execute('SELECT * FROM events;')
      rows = cur.fetchall()
      cur.close()
      conn.close()

      events = []
      for row in rows:
          events.append({'id': row[0], 'name': row[1], 'date': str(row[2])})
      return jsonify(events)
  ```

- Update the `/events` POST route to insert data into the database:

  ```python
  @app.route('/events', methods=['POST'])
  def create_event():
      new_event = request.get_json()
      name = new_event.get('name')
      date = new_event.get('date')

      conn = get_db_connection()
      cur = conn.cursor()
      cur.execute('INSERT INTO events (name, date) VALUES (%s, %s) RETURNING id;', (name, date))
      event_id = cur.fetchone()[0]
      conn.commit()
      cur.close()
      conn.close()

      new_event['id'] = event_id
      return jsonify(new_event), 201
  ```

- Ensure you handle exceptions and errors appropriately.

**3. Initialize the Database Schema:**

- Create an SQL script to initialize the database schema:

  - In the root directory, create a folder `db_init` if it doesn't exist.

    ```bash
    mkdir -p db_init/event_db
    ```

  - Create a file `init.sql` in `db_init/event_db/` with the following content:

    ```sql
    CREATE TABLE IF NOT EXISTS events (
      id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      date DATE NOT NULL
    );
    ```

- Update `docker-compose.yml` to run the initialization script:

  ```yaml
  event_db:
    image: postgres:13
    # ... other configurations ...
    volumes:
      - event_db_data:/var/lib/postgresql/data
      - ./db_init/event_db:/docker-entrypoint-initdb.d
  ```

  **Note:** PostgreSQL will execute any `*.sql` files in `/docker-entrypoint-initdb.d` during the first initialization.

**4. Update the Event Service Dockerfile:**

- Ensure all dependencies are installed in the Docker image.

- Update `Dockerfile`:

  ```dockerfile
  FROM python:3.9-slim

  WORKDIR /app

  RUN pip install Flask psycopg2-binary


  COPY . /app

  EXPOSE 5000

  CMD ["python", "app.py"]
  ```

**5. Rebuild and Restart the Containers:**

- Navigate back to the root project directory:

  ```bash
  cd ..
  ```

- Rebuild the Event Service:

  ```bash
  docker-compose build event_service
  ```

- Restart the services:

  ```bash
  docker-compose up -d
  ```

**6. Test the Event Service:**

- Access the API endpoint to retrieve events:

  ```bash
  curl http://localhost:5000/events
  ```

- Add a new event:

  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"name": "New Event", "date": "2023-11-01"}' \
  http://localhost:5000/events
  ```

- Verify that the event is stored in the database by retrieving all events.

#### **Instructions Part 2: Update User Service to Use the Database**

**1. Repeat Similar Steps for the User Service:**

- Navigate to the `user_service` directory:

  ```bash
  cd user_service
  ```

- Activate the virtual environment:

  ```bash
  source venv/bin/activate
  ```

- Install `psycopg2-binary`:

  ```bash
  pip install psycopg2-binary
  ```

- Update `requirements.txt` (or dockerfile `RUN pip install Flask psycopg2-binary`) accordingly.

**2. Modify `app.py` to Connect to PostgreSQL:**

- Set up environment variables for database connection.

- Update routes to interact with the database instead of in-memory data.

- Create a function `get_db_connection()` similar to the one in the Event Service.

- Implement CRUD operations for users in the database.

**3. Initialize the User Database Schema:**

- Create `init.sql` in `db_init/user_db/`:

  ```sql
  CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
  );
  ```

- Update `docker-compose.yml` to include the initialization script for `user_db`:

  ```yaml
  user_db:
    image: postgres:13
    # ... other configurations ...
    volumes:
      - user_db_data:/var/lib/postgresql/data
      - ./db_init/user_db:/docker-entrypoint-initdb.d
  ```

**4. Update the User Service Dockerfile:**

- Ensure dependencies are installed.

**5. Rebuild and Restart the Containers:**

- Rebuild the User Service:

  ```bash
  docker-compose build user_service
  ```

- Restart the services:

  ```bash
  docker-compose down --volumes
  docker-compose up -d
  ```

**6. Test the User Service:**

- Access the API endpoint to retrieve users:

  ```bash
  curl http://localhost:5001/users
  ```

- Add a new user:

  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"name": "Charlie", "email": "charlie@example.com"}' \
  http://localhost:5001/users
  ```

- Verify that the user is stored in the database.

---

#### **Instructions Part 3: Update Inter-Service Communication (Optional)**

- Ensure that when the User Service requests event data from the Event Service, it now retrieves data from the database.

- Test the endpoint:

  ```bash
  curl http://localhost:5001/users/1/events
  ```

---

**Deliverables:**

- Updated microservices (`event_service` and `user_service`) connected to their respective PostgreSQL databases.

- CRUD operations implemented in the microservices to interact with the databases.

- Updated `Dockerfile`, `docker-compose.yml`, and source code.

- A brief report or notes summarizing:

  - How you connected the microservices to the databases.
  - How you implemented data persistence with Docker volumes.
  - Challenges faced and solutions.
  - Key learnings from the exercise.

---

### **Final thoughts:**

- **Error handling:**

  - Implement try-except blocks to handle database exceptions.
  - Return appropriate HTTP status codes and messages.

- **Security warning:**

  - Be cautious with storing credentials in `docker-compose.yml`.
  - In production, consider using Docker secrets or environment variable management tools.

- **Database migrations:**

  - For schema changes, consider using migration tools like Alembic or Flask-Migrate.

- **Logging:**

  - Implement logging to track API calls and database operations.

- **Testing:**

  - Write tests for your CRUD operations to ensure they work as expected.

- **Docker Networking:**

  - Ensure that services can communicate over the `eventhive-network`.
  - Use service names defined in Docker Compose for hostnames.

- **Cleanup:**

  - Remember to deactivate your virtual environments:

    ```bash
    deactivate
    ```

  - To stop and remove containers:

    ```bash
    docker-compose down
    ```
