# Service Architecture (Docker Compose - Multi Container App)

## Overview

This setup consists of three main services:

- client (React frontend)
- backend (Node.js server)
- mongo (MongoDB database)

All services run inside separate Docker containers but are connected through Docker Compose.

---

## Architecture

client → backend → mongo

- Client sends request to backend
- Backend processes request and interacts with MongoDB
- MongoDB stores and retrieves data

---

## Communication

- Containers communicate using service names
- backend connects to Mongo using:
  mongodb://mongo:27017/dbname
- No need for localhost inside containers

---

## Networking

- Docker Compose creates a default network
- All services are part of the same network
- Services can directly talk using their names

---

## Ports

- client → exposed to browser (e.g., localhost:3000)
- backend → exposed for API (e.g., localhost:5000)
- mongo → usually not exposed externally

---

## Volumes (Persistence)

- MongoDB uses volume for data storage
- Data remains safe even if container stops or restarts

---

## Flow

1. User opens frontend in browser  
2. Frontend sends API request to backend  
3. Backend processes request  
4. Backend reads/writes data from MongoDB  
5. Response is sent back to frontend  

---

## Key Points

- Each service runs in isolation (separate container)
- Services communicate via Docker network
- Volumes ensure data persistence
- One command runs entire system:
  docker compose up -d

---

## Summary

This architecture demonstrates how multiple services (frontend, backend, database) can run together using Docker Compose with proper networking, communication, and persistent storage.