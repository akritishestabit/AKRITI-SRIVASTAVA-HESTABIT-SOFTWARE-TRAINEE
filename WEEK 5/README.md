# Week 5 – Docker (Complete Summary)

## Overview

This week focuses on understanding Docker from basics to a production-ready setup.
The goal was to build, run, and manage applications using containers, and gradually introduce concepts like networking, reverse proxy (NGINX), HTTPS, and production practices.

---

# Day 1 – Basic Docker (Single Container)

## Goal

Run a simple Node.js application inside a Docker container.

## Concepts Covered

* Dockerfile basics: `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`
* Difference between Image and Container
* Port mapping (`-p host:container`)

## Flow

```
Browser → Docker Container → Node Application
```

---

# Day 2 – Multi-Service Application (Docker Compose)

## Goal

Run multiple services (frontend, backend, database) together.

## Concepts Covered

* `docker-compose.yml`
* Defining multiple services
* Docker internal networking
* Service-to-service communication using service names

## Flow

```
Client → Backend → MongoDB
```

---

# Day 3 – NGINX and Load Balancing

## Goal

Use NGINX as a reverse proxy and distribute traffic across multiple backend containers.

## Concepts Covered

* Reverse proxy
* Upstream servers
* Load balancing (Round Robin, Least Connections)
* Multiple backend containers

## Flow

```
Browser → NGINX → backend1 / backend2
```

---

# Day 4 – HTTPS (SSL and TLS)

## Goal

Secure communication between client and server using HTTPS.

## Concepts Covered

* Difference between HTTP and HTTPS
* TLS (Transport Layer Security)
* SSL certificates (using mkcert for local development)
* SSL termination at NGINX
* HTTP to HTTPS redirection

## Flow

```
Browser → TCP → TLS → NGINX → Backend
```

---

# Day 5 – Production Setup

## Goal

Prepare the application for production use.

## Concepts Covered

* Environment variables using `.env`
* Restart policies (`restart: always`)
* Health checks
* Logging and log rotation
* Volumes for data persistence
* Production Docker Compose configuration

## Flow

```
User → HTTPS → NGINX → Backend → Database
```

---

# Key Takeaways

* Docker helps maintain consistency across environments.
* Docker Compose simplifies managing multi-service applications.
* NGINX acts as a reverse proxy, load balancer, and entry point.
* HTTPS ensures secure communication using encryption.
* Production setups require reliability features like monitoring, logging, and restart mechanisms.

---

# Final Summary

```
Dockerfile → Image → Container
Docker Compose → Multi-service system
NGINX → Reverse proxy and load balancing
HTTPS → Secure communication
Production → Reliable and scalable system
```

---

# Interview Summary Line

“I worked on building a containerized application using Docker and Docker Compose, implemented NGINX as a reverse proxy with load balancing, secured communication using HTTPS, and added production-level features like health checks, logging, and environment management.”
