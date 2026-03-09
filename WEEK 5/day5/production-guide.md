# Production Deployment Guide

This project demonstrates a simple production-like deployment using Docker.

## Services Used

This setup runs three containers:

- backend1 → Node.js server
- backend2 → Node.js server
- nginx → reverse proxy and load balancer

Nginx receives all incoming requests and distributes them between the backend containers.

## How to Run the Project

To start the production setup, run:

./deploy.sh

This command will:

- build the Docker images
- start all containers
- run the application in the background

## Environment Variables

Environment variables are stored inside the `.env` file.

Example:

NODE_ENV=production  
PORT=3000

## Testing the Application

Open the browser and go to:

https://localhost

You will see a response from one container.

If you refresh the page multiple times, the container ID will change.
This confirms that load balancing is working correctly.

## Logs

This folder is reserved for storing application logs in future if logging is added.

## Conclusion

This setup simulates a production environment using:

- Docker
- Docker Compose
- Nginx reverse proxy
- Load balancing
- Environment variables