### **Exercise 1: Analyze and Deconstruct a Microservice Application**

*Duration: Approximately 70 minutes*

**What you'll get out of this exercise:**
Hands on experience with a microservices application to understand its architecture, components, and communication patterns.

**Instructions part 1 (individually):**

1. **Introduction to the Application (5 minutes):**

   - We will be using the **[Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo)** by Google Cloud Platform, a cloud native microservices demo application.
   - This application consists of multiple microservices written in different languages, showcasing a typical e-commerce website.
   - Go ahead and explore the application on GitHub (or clone it and do this locally).

2. **Setting Up the Environment (10 minutes):**

   - **Clone the Repository:**
     ```bash
     git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
     ```
   - **Navigate to the Project Directory:**
     ```bash
     cd microservices-demo
     ```
   - **Explore the Repository Structure:**
     - Familiarize yourself with the directories and files.
     - Note the different services located in the `src/` directory.

3. **Understanding the Architecture (15 minutes):**

   - **Review the Architectural Diagram:**
     - Locate the architecture diagram in the repository or view it [here](https://github.com/GoogleCloudPlatform/microservices-demo#architecture).
     - Identify each microservice and its role within the application.
   - **List of Microservices:**
     - Frontend Service
     - Product Catalog Service
     - Cart Service
     - Recommendation Service
     - Checkout Service
     - Payment Service
     - Shipping Service
     - Email Service
     - Ad Service
     - Currency Service

**Instructions part 2 (subgroup):**

4. **Dive into Services (20 minutes):**

   - **Select Two Microservices to Analyze:**
     - Choose any two services that interest you.
   - **For Each Service:**
     - **Examine the Codebase:**
       - Open the service's directory and review the code.
       - Identify the main components and dependencies.
     - **API Endpoints:**
       - Locate the API definitions or protobuf files.
       - Understand what endpoints the service exposes.
     - **Communication Patterns:**
       - Determine how the service communicates with others (e.g., REST, gRPC).
       - Identify any message formats or protocols used.
     - **Data Management:**
       - Note if the service interacts with a database or external data source.
       - Understand how data is stored and retrieved.

5. **Interservice Communication (10 minutes):**

   - **Trace a User Request Flow:**
     - Start from the frontend service and follow how a user action (like adding an item to the cart) propagates through the system.
     - Identify which services are involved and the sequence of interactions.
   - **Fault Tolerance and Resilience:**
     - Observe any mechanisms in place for handling failures (e.g., retries, circuit breakers).

**Instructions part 3 (when we're back in the main room):**

6. **Back in the main room (5 minutes):**
     - Have a person speaking on behalf of the group.
     - Share your findings and insights.
     - Discuss any challenges or interesting patterns you observed, and feel free to share uncertainties or questions you might have.

7. **Reflection and Documentation (Final 5 minutes):**

   - **Summarize Your Learnings:**
     - Write down key takeaways about microservices architecture from this exercise.
     - Note any questions or topics you wish to explore further.


