
### **Exercise 2: Design a Microservices Architecture for an Event Ticketing Platform**

*Duration: Approximately 75 minutes*

**What you'll get out of this exercise:**
Practice with applying microservices design principles to architect a scalable, modular event ticketing platform.

**Instructions part 1 (individually):**

1. **Understand the Business Requirements (10 minutes):**

   - **Scenario Overview:**
     - You are tasked with designing the backend architecture for **"EventHive"**, a platform that sells tickets for events such as concerts, conferences, and sports games.
     - Key functionalities include user authentication, event management, ticket sales, payment processing, notifications, and analytics.
     - The system must handle high traffic during peak times and ensure data consistency and reliability.
     - You need to create a visual architectural diagram which shows your microservices and their interactions.
   - **Deliverables:**
     - An architectural diagram of your proposed microservices system.
     - A brief written summary detailing:
        - The microservices you've identified.
        - The responsibilities of each microservice.
        - Communication patterns and protocols used.
        - Data management strategies.
        - Scalability and resilience considerations.

2. **Identify Core Services (5-10 minutes):**

   - **List Potential Microservices:**
     - Which functionalities does the application have? Which services would you create?
   - **Define Boundaries:**
     - Ensure each service has a single responsibility and can be developed, deployed, and scaled independently.

3. **Define Service Responsibilities (15 minutes):**

   - **For Each Service:**
     - **Primary Functions:**
       - Describe what the service does.
     - **Data Ownership:**
       - Identify the data it manages and how it stores it.
     - **APIs and Interfaces:**
       - Outline the endpoints it exposes and the expected inputs/outputs.
     - **Interservice Communication:**
       - Determine which other services it needs to communicate with and how.

4. **Design Interservice Communication (10 minutes):**

   - **Communication Patterns:**
     - Decide between synchronous (RESTful APIs, gRPC) and asynchronous (message queues, event buses) communication.
   - **Integration Points:**
     - Map out how services will interact during a typical user flow, such as purchasing a ticket.
   - **Error Handling:**
     - Plan for retries, fallbacks, and how to handle failed communications.

5. **Data Management Strategy (5 minutes):**

   - **Database Design:**
     - Choose between shared databases or per-service databases.
     - Consider data replication and synchronization strategies.
   - **Consistency Models:**
     - Decide on eventual consistency vs. strong consistency where appropriate.

6. **(Optional given time) Scalability and Resilience (5 minutes):**

   - **Deployment Considerations:**
     - Plan for containerization using Docker.
     - Consider orchestration tools like Kubernetes for scaling.
   - **Resilience Mechanisms:**
     - Implement load balancing, health checks, and auto-scaling policies.

**Instructions part 2 (sub groups):**

7. **Show your work to your colleagues in the breakout room (15 minutes):**

   - **Questions and discussion:**
     - Share screens and show your work, be open about points of doubts, things you may not understand well enough yet and of course elements that you're proud of.
     - Ask each other questions and answer questions others might have.
   - **Adapt to New Insights:**
     - There are likely parts you've seen that you did not think about. Or ways to optimize a solution you choose. Go ahead and make the changes to your design.

**Instructions part 3 (back in the main room):**

8. **Present Your Architecture (Final 5 minutes):**

   - **Show your Architectural Diagram:**
     - Explain how you visualized your microservices and their interactions.
   - **Summary:**
     - Be ready to explain your design choices and how they meet the business requirements.

9. **Reflection and Documentation (Final 5 minutes):**

   - **Summarize Your Learnings:**
     - Write down key takeaways about microservices architecture from this exercise.
     - Note any questions or topics you wish to explore further.



