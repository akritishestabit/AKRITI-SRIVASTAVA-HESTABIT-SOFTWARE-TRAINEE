# NGINX Reverse Proxy and Load Balancing

In this setup we use NGINX as a reverse proxy in front of our backend servers.

## Reverse Proxy

A reverse proxy is a server that sits between the user and the backend servers.  
When a user sends a request, it first goes to NGINX. After that, NGINX forwards the request to one of the backend containers.

So the user does not directly communicate with the backend server.

Flow:

User → NGINX → Backend

## Backend Containers

In this project we run two backend containers:

- backend1
- backend2

Both containers run the same Node.js application.

## Load Balancing

Load balancing means distributing requests across multiple servers so that no single server gets overloaded.

Here we use **round-robin load balancing**.  
NGINX sends requests to backend containers one by one.

Example:

Request 1 → backend1  
Request 2 → backend2  
Request 3 → backend1  
Request 4 → backend2  

This helps improve performance and makes the system more reliable.

## How the System Works

1. The user opens `http://localhost:8080`.
2. The request goes to the NGINX container.
3. NGINX forwards the request to one of the backend containers.
4. The backend processes the request and sends the response back.

## Files Used

- `docker-compose.yml` → runs all containers together  
- `nginx.conf` → NGINX configuration for routing requests  
- `server.js` → backend application

## Conclusion

NGINX works as a reverse proxy and distributes traffic between multiple backend containers.  
This setup is commonly used in real production environments to handle large numbers of requests.d