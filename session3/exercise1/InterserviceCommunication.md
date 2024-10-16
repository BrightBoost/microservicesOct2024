### **Exercise 2: Implementing Interservice Communication**

*Duration: Approximately 60 minutes*

**What you'll get out of this exercise:**

- Implement RESTful interservice communication between microservices.
- Understand how microservices interact within a Docker network.
- Use environment variables for configuration, adhering to Twelve-Factor App principles.

---

#### **Background:**

In this exercise, you will enhance your microservices to allow the User Service to interact with the Event Service. Specifically, the User Service will retrieve event information from the Event Service to show events that a user might be interested in.

---

#### **Instructions Part 1: Implement Interservice Communication**

**1. Modify the User Service to Communicate with the Event Service (25 minutes):**

   - **Objective:** Allow the User Service to fetch event data from the Event Service.

   - **Steps:**
     - In `user_service/app.py`, add necessary imports:
       ```python
       import os
       import requests
       ```
     - Define the Event Service URL using an environment variable:
       ```python
       EVENT_SERVICE_URL = os.environ.get('EVENT_SERVICE_URL', 'http://event_service:5000')
       ```
     - Add a new route to get events for a user:
       ```python
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
       ```
     - **Note:** This simulates fetching events for a user. In a real application, you'd filter events based on user preferences or registrations.

   - **Update Dockerfile to Include Requests Library:**
     - In the `user_service` Dockerfile, update the `RUN` command:
       ```dockerfile
       RUN pip install Flask requests
       ```

   - **Rebuild the Docker Image:**
     ```bash
     docker build -t user_service:latest .
     ```

**2. Use Environment Variables for Configuration (5 minutes):**

   - **Objective:** Configure the Event Service URL using environment variables.

   - **Update the Docker Run Command for User Service:**
     ```bash
     docker run -d --name user_service --network eventhive-network -p 5001:5001 \
     -e EVENT_SERVICE_URL='http://event_service:5000' \
     user_service:latest
     ```

**3. Ensure the Event Service is Running:**

   - If the Event Service is not running, start it:
     ```bash
     docker run -d --name event_service --network eventhive-network -p 5000:5000 event_service:latest
     ```

**4. Test the Interservice Communication (15 minutes):**

   - **Verify Both Services Are Running:**
     ```bash
     docker ps
     ```

   - **Test the New Endpoint:**
     - Access `http://localhost:5001/users/1/events` to get events for user with ID 1.

   - **Expected Response:**
     - The response should include the user's information and a list of events fetched from the Event Service.

---

#### **Instructions Part 2: Enhancing Services and Configuration**

**5. Add Error Handling and Logging (10 minutes):**

   - **Objective:** Improve the robustness of your services.

   - **Steps:**
     - In both services, add logging to track requests and errors.
     - Use Python's built-in `logging` module.
     - Example in `user_service/app.py`:
       ```python
       import logging

       logging.basicConfig(level=logging.INFO)

       # Inside your route functions
       logging.info(f'Fetching events for user {user_id}')
       ```

**6. Use Docker Compose for Simplified Management (Optional, 15 minutes):**

   - **Objective:** Use Docker Compose to manage multiple containers.

   - **Steps:**
     - Create a `docker-compose.yml` file in the root `eventhive-microservices` directory:
       ```yaml
       version: '3'
       services:
         event_service:
           build: ./event_service
           ports:
             - "5000:5000"
           networks:
             - eventhive-network
         user_service:
           build: ./user_service
           ports:
             - "5001:5001"
           environment:
             - EVENT_SERVICE_URL=http://event_service:5000
           depends_on:
             - event_service
           networks:
             - eventhive-network
       networks:
         eventhive-network:
           driver: bridge
       ```

     - Use Docker Compose to build and run services:
       ```bash
       docker-compose up --build
       ```

   - **Test the Services:**
     - Access `http://localhost:5001/users/1/events`.

---

#### **Deliverables:**

- Enhanced User Service that communicates with the Event Service.
- Services configured using environment variables and/or Docker Compose.
- A brief report or notes summarizing:
  - How you implemented interservice communication.
  - Challenges faced and solutions.
  - Key learnings from the exercise.

---

### **Additional Notes:**

- **Error Handling:**
  - Implement try-except blocks to handle exceptions.
  - Return appropriate HTTP status codes.

- **Logging:**
  - Use structured logging for better observability.
  - Redirect logs to stdout/stderr as per Twelve-Factor App principles.

- **Cleanup:**
  - Deactivate virtual environments:
    ```bash
    deactivate
    ```
  - Remove Docker containers and images if needed:
    ```bash
    docker-compose down
    docker rmi event_service:latest user_service:latest
    ```

