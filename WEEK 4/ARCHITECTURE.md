# Week 4 – Day 1 Backend Architecture

## 1. Overview

This backend system is designed using a structured and modular approach.
The goal of Day 1 was not to build APIs, but to build a proper backend boot system.

Instead of directly starting an Express server, we implemented a controlled lifecycle
where each dependency loads in a defined order.

This ensures production-level safety and clarity.

---

## 2. Boot Lifecycle Flow

The server follows this startup sequence:

server.js
  ↓
Load environment configuration
  ↓
Initialize logger
  ↓
Connect database
  ↓
Load Express app
  ↓
Load middlewares
  ↓
Mount routes
  ↓
Start server
  ↓
Enable graceful shutdown

This ensures that the server does not start unless all critical components are ready.

---

## 3. Folder Structure Philosophy

The project follows strict separation of concerns:

src/
  config/        → Environment configuration loader
  loaders/       → App & database boot logic
  models/        → Database schemas (future use)
  routes/        → Route definitions (future use)
  controllers/   → Request handlers (future use)
  services/      → Business logic layer (future use)
  repositories/  → Database abstraction layer (future use)
  middlewares/   → Cross-cutting concerns (future use)
  utils/         → Logger and shared utilities
  jobs/          → Background workers (future use)
  logs/          → Log storage

This structure ensures scalability and clean architecture.

---

## 4. Config Loader

The configuration system:

- Supports multiple environments:
  - .env.local
  - .env.dev
  - .env.prod
- Validates required environment variables
- Prevents hardcoded values
- Follows environment isolation principle

If required variables are missing, the system fails immediately.

---

## 5. Logger System

We implemented structured logging using Winston.

Features:
- Console logging
- File logging (/src/logs/app.log)
- JSON formatted logs
- Environment-based log level

This improves debugging and production monitoring.

---

## 6. Database Loader

The database loader:

- Connects to MongoDB before server start
- Uses fail-fast strategy
- Stops server if DB connection fails

This prevents partial system execution.

---

## 7. App Loader

The app loader:

- Initializes Express
- Loads security middlewares (Helmet, CORS)
- Parses JSON bodies
- Mounts routes
- Logs number of mounted endpoints

This keeps server.js clean and focused only on orchestration.

---

## 8. Graceful Shutdown

The system listens for SIGINT.

On shutdown:
- Stops accepting new requests
- Closes server safely
- Exits process cleanly

This prevents memory leaks and unstable termination.

---

## 9. Production Engineering Principles Applied

✔ Separation of concerns  
✔ Dependency orchestration  
✔ Environment isolation  
✔ Fail-fast validation  
✔ Structured logging  
✔ Graceful shutdown handling  

