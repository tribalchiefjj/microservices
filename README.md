# Online Auction Microservices Project

## Overview

This project is a **microservices-based online auction system** designed for scalability, modularity, and ease of deployment. I used  **Docker**, **Flask**, **PostgreSQL**, and microservice communication patterns to ensure a robust and maintainable architecture.

## Key Technologies And Tech complexity

### 1. **Microservices Architecture**

- Designed and implemented **separate services** for user management, auctions, bidding, and notifications.
- Each service operates **independently** and communicates as needed, improving scalability.

### 2. **User Authentication & JWT Security**

- Implemented **JWT-based authentication** for secure user login.

### 3. **Database Integration & Dockerized PostgreSQL**

- Each service interacts with a **PostgreSQL database**, and we used Docker Compose to ensure database persistence across container restarts.
- Created robust database connection handling to prevent failures during requests.

### 4. **Containerization with Docker**

- Every service runs in a **Docker container**, making deployment and scaling easier.
- Configured **Docker Compose** to manage multiple services and ensure seamless interaction between them.

### 5. **Testing & Debugging**

- Used **Pytest** for automated unit and integration testing.
- Overcame challenges related to database connectivity within Docker and improved local testing with environment-based configurations.

## What am still working on :

### 1. **Bidding Service (Real-Time Bidding)**

- Implement real-time bidding functionality using **WebSockets or a message queue (RabbitMQ/Kafka)**.
- Ensure that bid updates are **instant** for all users in an auction.

### 2. **Notification Service**

- Send **email or in-app notifications** when a user is outbid or wins an auction.
- Integrate with an SMTP service or third-party notification provider.

✅ **Future-proof architecture** to integrate WebSockets & real-time updates.


### 3. **Frontend actually not something i wanna do but for a UI for non techies(its a bonus tho, i love bonuses)**

- Create a ** frontend** to allow users to interact with the auction system.
- Build a clean, modern UI with real-time bid updates.

### 4. **Deployment**


