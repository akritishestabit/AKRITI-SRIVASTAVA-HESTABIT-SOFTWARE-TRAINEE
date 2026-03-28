# Production Guide — Fullstack Docker Application

## Overview

This project is a simple production-ready fullstack application using Docker.

It includes:
- Frontend (HTML served by NGINX)
- Backend (Node.js API)
- MongoDB (Database)
- NGINX (Reverse proxy + HTTPS)

All services run together using Docker Compose.

---

## Architecture Flow

Browser (https://localhost)
        ↓
NGINX
   ├── / → serves frontend (index.html)
   └── /api → routes to backend
                    ↓
                Backend (Node.js)
                    ↓
                MongoDB

---

## Features Implemented

- HTTPS using self-signed certificates (mkcert)
- Reverse proxy using NGINX
- Environment variables using .env
- Health check for backend service
- Restart policy for reliability
- Volume for MongoDB data persistence
- Log rotation for backend

---

## Environment Variables

Stored in `.env` file:

Purpose:
- Avoid hardcoding sensitive data
- Easy configuration management

---

## Health Check

Backend includes a health endpoint:

/health → returns OK

Docker uses this to verify container status.

---

## Logging

Logging is enabled for backend:

- Limits log file size
- Prevents disk overflow
- Helps in debugging errors

---

## SSL Setup

Certificates generated using mkcert:

mkcert -install  
mkcert localhost  

Files:
- localhost.pem
- localhost-key.pem

Used by NGINX to enable HTTPS.

---

## Running the Application

Run the following command:

docker compose -f docker-compose.prod.yml up -d --build

---

## Access

Open in browser:

https://localhost

---

## Key Design Decisions

- Used a single NGINX container for both frontend and reverse proxy
- Avoided separate frontend container for simplicity
- Used volumes to serve static files
- Focused logging on backend only

---

## Conclusion

This setup demonstrates a production-style Docker deployment with:

- Secure communication (HTTPS)
- Service isolation (containers)
- Automated restart and monitoring
- Clean and simple architecture
