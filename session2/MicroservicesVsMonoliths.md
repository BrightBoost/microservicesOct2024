### **Exercise 2: Microservices vs. Monoliths**

*Duration: Approximately 75 minutes*

**What you'll get out of this exercise:**

Compare and contrast monolithic and microservices architectures by analyzing an application implemented in both styles, incorporating the principles of the Twelve-Factor App methodology.

**Instructions Part 1 (Individually):**

1. **Introduction to the Application (5 minutes):**

   - We will be using the **[eShopOnWeb](https://github.com/dotnet-architecture/eShopOnWeb)** (monolithic version) and **[eShopMicroservices](https://github.com/dotnet/eShop)** (microservices version) applications developed by Microsoft.
   - These are sample applications that represent an e-commerce system implemented as a monolith and as microservices, respectively.

2. **Setting Up the Environment (10 minutes):**

   - **Clone the Monolithic Repository:**
     ```bash
     git clone https://github.com/dotnet-architecture/eShopOnWeb.git
     ```
   - **Clone the Microservices Repository:**
     ```bash
     git clone https://github.com/dotnet-architecture/eShopOnContainers.git
     ```
   - **Explore the Repository Structures:**
     - Familiarize yourself with the directories and files in both repositories.
     - Note the differences in structure and organization.

3. **Understanding the Twelve-Factor App Methodology (10 minutes):**

   - **Review the Twelve Factors:**
     - Codebase, Dependencies, Config, Backing Services, Build/Run, Processes, Port Binding, Concurrency, Disposability, Dev/Prod Parity, Logs, Admin Processes.
   - **Consider How Each Application Aligns with These Principles:**
     - Identify which factors are better addressed in the microservices version.

**Instructions Part 2 (Subgroup):**

4. **Comparative Analysis (30 minutes):**
   - **Prepare to Present your Report in the Main Room:**
     - You can use diagrams, slide tools or a plain google doc that includes your report. Make sure to have written down considerations for each choice.
   - **Architecture Comparison:**
     - **Monolithic Application:**
       - Identify the layers and how they interact.
       - Discuss deployment as a single unit.
     - **Microservices Application:**
       - Identify the individual services and their responsibilities.
       - Discuss how services communicate (e.g., REST, messaging).
   - **Deployment and Scaling:**
     - **Monolith:**
       - Consider the challenges in scaling and deploying.
     - **Microservices:**
       - Analyze how containerization and orchestration (e.g., Docker, Kubernetes) facilitate deployment and scaling.
   - **Maintenance and Development:**
     - **Monolith:**
       - Discuss how changes affect the entire application.
     - **Microservices:**
       - Explore how independent services allow for isolated development and deployment.

5. **Applying the Twelve-Factor App Principles (15 minutes):**

   - **Identify Compliance:**
     - For each factor, note how the microservices application adheres to the principle better than the monolith.
   - **Examples:**
     - **Dependencies:** Microservices explicitly declare dependencies, facilitating isolation.
     - **Config:** Microservices manage configuration per service, enhancing flexibility.
     - **Logs:** Microservices treat logs as event streams, aiding in centralized monitoring.

**Instructions Part 3 (Back in the Main Room):**

6. **Group Discussion (10 minutes):**

   - **Share Insights:**
     - Discuss the key differences observed.
     - Reflect on how the Twelve-Factor App principles are applied in each architecture.

7. **Reflection and Documentation (Final 5 minutes):**

   - **Summarize Learnings:**
     - Write down key takeaways regarding the advantages and trade-offs between monoliths and microservices.
     - Note any questions for further exploration.




