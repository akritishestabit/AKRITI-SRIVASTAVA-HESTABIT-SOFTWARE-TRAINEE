# Linux in Container (Docker Fundamentals)

## Goal

Understand how Docker containers work internally as a Linux environment and how applications run inside them.

---

## What We Built

- A simple Node.js server
- Containerized using Docker
- Ran the app inside a container

---

## Core Concepts

- Image → blueprint of application  
- Container → running instance of image  
- Volumes → persistent storage  
- Network → communication between containers  

---

## Dockerfile Overview

- FROM node:18 → base Linux image  
- WORKDIR /app → working directory inside container  
- COPY package*.json → copy dependencies  
- RUN npm install → install packages  
- COPY app/ . → copy source code  
- EXPOSE 3000 → define port  
- CMD ["node", "server.js"] → start server  

---

## Running the Container

- Build image  
  docker build -t app-name .

- Run container  
  docker run -p 3002:3000 app-name

---

## Entering Container (Linux Access)

docker exec -it <container> /bin/sh

This allows access to the container like a Linux terminal.

---

## Linux Exploration Inside Container

Commands used:

- ls → view files and folders  
- ps → check running processes  
- top → monitor CPU and memory usage  
- df -h → check disk usage  
- logs → view application logs  

---

## Key Learnings

- Container is a lightweight Linux system  
- Each container has its own processes and filesystem  
- Node app runs as a process inside container  
- Ports expose container services to host  
- Logs help in debugging  

---

## Summary

Docker containers simulate a Linux environment where applications run in isolation. We explored how to build, run, and inspect containers using basic Linux commands.