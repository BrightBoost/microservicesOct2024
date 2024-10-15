### **Exercise 1: Analyze and Deconstruct a Monolithic Application**

*Duration: Approximately 60 minutes*

**What you'll get out of this exercise:**
Practical experience in understanding the structure of a monolithic application, its components, and how it differs from microservices architecture in terms of deployment, development, and maintenance.

**Instructions Part 1 (Individually):**

1. **Introduction to the Monolithic Application (5 minutes):**

   - We will be using the **[Spring PetClinic](https://github.com/spring-projects/spring-petclinic)** application.
   - This is a classic monolithic web application built using Spring Framework, simulating a simple pet clinic system.

2. **Setting Up the Environment (10 minutes):**

   - **Clone the Repository:**
     ```bash
     git clone https://github.com/spring-projects/spring-petclinic.git
     ```
   - **Navigate to the Project Directory:**
     ```bash
     cd spring-petclinic
     ```
   - **Explore the Repository Structure:**
     - Familiarize yourself with the directories and files.
     - Note the structure of controllers, services, repositories, and domain models.

3. **Understanding the Architecture (10 minutes):**

   - **Review the Application Layers:**
     - **Presentation Layer:** Controllers and views handling HTTP requests and responses.
     - **Service Layer:** Business logic encapsulated in service classes.
     - **Data Access Layer:** Repositories interacting with the database.
     - **Domain Models:** Entities representing the data structures.
   - **Deployment Model:**
     - Note that the entire application is packaged and deployed as a single unit (typically a WAR or JAR file as it's Java).

**Instructions Part 2 (Subgroup):**

4. **Discuss Components (10 minutes):**
   - **Prepare to Present your Report in the Main Room:**
     - You can use diagrams, slide tools or a plain google doc that includes your report. Make sure to have written down considerations for each choice.
   - **Identify Core Functionalities:**
     - **Owners Management:** Viewing and editing pet owners.
     - **Pets Management:** Adding and managing pets.
     - **Appointments:** Scheduling and viewing appointments.
   - **Analyze the Codebase:**
     - **Controllers:** Look at how HTTP requests are mapped and handled.
     - **Services:** Understand how business logic is implemented.
     - **Repositories:** Examine how data persistence is managed.
   - **Data Flow:**
     - Trace how data flows from the presentation layer to the database and back.

5. **Deployment and Maintenance Considerations (10 minutes):**

   - **Deployment Process:**
     - Discuss how changes require rebuilding and redeploying the entire application.
   - **Scalability:**
     - Consider the challenges in scaling specific components of the application.
   - **Technology Stack:**
     - Note that the application uses a consistent technology stack throughout.

**Instructions Part 3 (Back in the Main Room):**

6. **Group Discussion (5 minutes):**

   - **Share Findings:**
     - Discuss any challenges or interesting observations.
     - Reflect on how the monolithic structure impacts development and maintenance.

7. **Reflection and Documentation (5 minutes):**

   - **Summarize Your Learnings:**
     - Write down key takeaways about monolithic architecture from this exercise.
     - Note any questions or topics you wish to explore further.

