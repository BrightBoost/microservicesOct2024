### **Exercise 1: Implement and Containerize Two Microservices Based on an Event Ticketing Platform**

*Duration: Approximately 70 minutes*

**What you'll get out of this exercise:**

- Learn how to build basic microservices in Python.
- Understand how to write Dockerfiles and build Docker images.
- Gain hands-on experience with basic Docker commands.
- Run containers locally to test your microservices.

---

#### **Background:**

In this exercise, you will create two microservices that represent core functionalities of an event ticketing platform called **"EventHive"**:

1. **Event Service**: Manages event information (e.g., concerts, conferences).
2. **User Service**: Manages user information (e.g., user registration and profiles).

You will implement each service independently and containerize them using Docker. The services will not communicate with each other in this exercise.

---

#### **Instructions Part 1: Implement Two Microservices**

**1. Set Up Your Development Environment (5 minutes):**

   - Ensure you have **Python 3.7+** installed.
   - Install **Docker** on your machine if not already installed.
   - Choose a code editor or IDE you're comfortable with (e.g., VSCode, PyCharm).

**2. Create a Project Directory (5 minutes):**

   - Create a new directory for your project:
     ```bash
     mkdir eventhive-microservices
     cd eventhive-microservices
     ```
   - Within this directory, create two subdirectories: `event_service` and `user_service`.

**3. Implement the Event Service (30 minutes):**

   - Navigate to the `event_service` directory:
     ```bash
     cd event_service
     ```
   - Create a Python virtual environment (optional but recommended):
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install Flask:
     ```bash
     pip install Flask
     ```
   - Create a file named `app.py` and add the following code:

     ```python
     from flask import Flask, jsonify, request

     app = Flask(__name__)

     events = [
         {'id': 1, 'name': 'Concert A', 'date': '2023-11-01'},
         {'id': 2, 'name': 'Conference B', 'date': '2023-12-15'}
     ]

     @app.route('/events', methods=['GET'])
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
         app.run(host='0.0.0.0', port=5000)
     ```

   - **Test the Microservice Locally:**
     - Run the service:
       ```bash
       python app.py
       ```
     - Use `curl` or Postman to test the endpoints:
       - Get all events: `GET http://localhost:5000/events`
       - Get an event by ID: `GET http://localhost:5000/events/1`
       - Create a new event: `POST http://localhost:5000/events` with JSON body

**4. Implement the User Service (30 minutes):**

   - Navigate to the `user_service` directory:
     ```bash
     cd ../user_service
     ```
   - Create a Python virtual environment (optional but recommended):
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install Flask:
     ```bash
     pip install Flask
     ```
   - Create a file named `app.py` and add the following code:

     ```python
     from flask import Flask, jsonify, request

     app = Flask(__name__)

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

     @app.route('/users', methods=['POST'])
     def create_user():
         new_user = request.get_json()
         users.append(new_user)
         return jsonify(new_user), 201

     if __name__ == '__main__':
         app.run(host='0.0.0.0', port=5001)
     ```

   - **Test the Microservice Locally:**
     - Run the service:
       ```bash
       python app.py
       ```
     - Use `curl` or Postman to test the endpoints:
       - Get all users: `GET http://localhost:5001/users`
       - Get a user by ID: `GET http://localhost:5001/users/1`
       - Create a new user: `POST http://localhost:5001/users` with JSON body

---

#### **Instructions Part 2: Containerize the Microservices**

**5. Write Dockerfiles for Each Service (20 minutes):**

   - **Event Service Dockerfile:**
     - Navigate to the `event_service` directory.
     - Create a file named `Dockerfile` and add the following content:

       ```dockerfile
       # Use an official Python runtime as a parent image
       FROM python:3.9-slim

       # Set the working directory in the container
       WORKDIR /app

       # Copy the current directory contents into the container at /app
       COPY . /app

       # Install any needed packages
       RUN pip install Flask

       # Make port 5000 available to the world outside this container
       EXPOSE 5000

       # Run app.py when the container launches
       CMD ["python", "app.py"]
       ```

   - **User Service Dockerfile:**
     - Navigate to the `user_service` directory.
     - Create a file named `Dockerfile` and add the following content:

       ```dockerfile
       # Use an official Python runtime as a parent image
       FROM python:3.9-slim

       # Set the working directory in the container
       WORKDIR /app

       # Copy the current directory contents into the container at /app
       COPY . /app

       # Install any needed packages
       RUN pip install Flask

       # Make port 5001 available to the world outside this container
       EXPOSE 5001

       # Run app.py when the container launches
       CMD ["python", "app.py"]
       ```

**6. Build Docker Images (10 minutes):**

   - **Event Service Image:**
     - Navigate to the `event_service` directory.
     - Build the Docker image:
       ```bash

       docker build -t event_service:latest .
       ```
   - **User Service Image:**
     - Navigate to the `user_service` directory.
     - Build the Docker image:
       ```bash
       docker build -t user_service:latest .
       ```

**7. Run the Containers Locally (15 minutes):**

   - **Create a Network for the Services:**
     ```bash
     docker network create eventhive-network
     ```

   - **Run the Event Service Container:**
     ```bash
     docker run -d --name event_service --network eventhive-network -p 5000:5000 event_service:latest
     ```

   - **Run the User Service Container:**
     ```bash
     docker run -d --name user_service --network eventhive-network -p 5001:5001 user_service:latest
     ```

   - **Test the Services:**
     - Access `http://localhost:5000/events` to test the Event Service.
     - Access `http://localhost:5001/users` to test the User Service.

**8. Troubleshooting (5 minutes):**

   - If you encounter any issues:
     - Use `docker logs <container_name>` to check container logs.
     - Ensure that the containers are running using `docker ps`.
     - Confirm that the Docker network is properly configured.

---

#### **Deliverables:**

- Two Dockerized microservices (Event Service and User Service) running locally.
- A brief report or notes summarizing:
  - The steps you took to build and containerize the services.
  - Any challenges faced and how you resolved them.
  - Key learnings from the exercise.


