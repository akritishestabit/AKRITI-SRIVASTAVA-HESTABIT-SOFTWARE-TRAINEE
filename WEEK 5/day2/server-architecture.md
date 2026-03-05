# Service Architecture

This project uses Docker Compose to run two services together: a backend server and a MongoDB database.

## Backend Service
The backend is built using Node.js and Express.  
It runs inside a Docker container and listens on port 5000.  
The backend handles requests from the user and communicates with the MongoDB database.

Example:
http://localhost:5000

## MongoDB Service
MongoDB runs in a separate Docker container using the official Mongo image.  
It stores the application data and runs on port 27017.

## Docker Compose
Docker Compose is used to start both containers together.  
It also automatically creates a network so that the backend container can communicate with the MongoDB container.

## Container Communication
The backend connects to MongoDB using the service name:

mongodb://mongo:27017

Here `mongo` is the service name defined in docker-compose.

## Application Flow

User → Backend (Node.js container) → MongoDB container

1. User sends a request to the backend.
2. Backend processes the request.
3. Backend communicates with MongoDB.
4. MongoDB returns the data.
5. Backend sends the response to the user.