# Week 4 Backend API

## Overview

This project is a production-ready backend system built using Node.js, Express, MongoDB, and Redis. It includes advanced API features, security practices, logging, request tracing, and background job processing.

---

## Architecture

```
src/
│── controllers/
│── services/
│── repositories/
│── models/
│── routes/
│── loaders/
│── middlewares/
│── utils/
│── jobs/
│── config/
```

The project follows a layered architecture:

* Controller → handles request/response
* Service → business logic
* Repository → database interaction

---

## Tech Stack

* Node.js
* Express.js
* MongoDB (Mongoose)
* Redis (BullMQ)
* Winston (logging)
* Morgan (HTTP logging)
* UUID (request tracing)
* Helmet, CORS, Rate Limit (security)

---

## Features

### Product APIs

* Create Product
* Get All Products
* Get Product by ID
* Update Product
* Delete Product (soft delete)

---

### Query Capabilities

* Search by name and description
* Filter by category
* Price range filtering
* Sorting (e.g. price:desc)
* Pagination (page, limit)

---

### Security

* Secure HTTP headers using Helmet
* Rate limiting
* CORS handling
* Input validation
* Soft delete protection

---

### Logging and Observability

* Structured logging using Winston
* HTTP request logging using Morgan
* Log files:

  * logs/combined.log
  * logs/error.log
* Request tracing using X-Request-ID
* Context-based logging using AsyncLocalStorage

---

### Background Jobs

* Implemented using BullMQ with Redis
* Email job simulation
* Retry mechanism with exponential backoff
* Worker-based processing

---

### Request Tracing

* Each request is assigned a unique ID
* ID is included in logs and response headers
* Helps in debugging and monitoring

---

## API Endpoints

### Products

```
POST    /products
GET     /products
GET     /products/:id
PUT     /products/:id
DELETE  /products/:id
```

### Query Examples

```
GET /products?search=Samsung
GET /products?sort=price:desc
GET /products?page=1&limit=5
GET /products?minPrice=50000&maxPrice=80000
```

### Background Job

```
POST /products/send-email
```

### Health Check

```
GET /health
```

---

## API Testing

A Postman collection is included in the repository under the docs folder. It contains all endpoints and uses environment variables:

* base_url
* product_id

---

## Logs

```
logs/
  ├── combined.log
  ├── error.log
```

These logs capture request activity, errors, and background job execution.

---

## Setup Instructions

### Install dependencies

```
npm install
```

### Configure environment

Create a `.env.dev` file:

```
PORT=5000
MONGO_URI=your_mongodb_url
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
LOG_LEVEL=info
```

### Start Redis

```
redis-server
```

### Run server

```
npm run dev
```

---

## Environment Example

```
PORT=5000
MONGO_URI=
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
LOG_LEVEL=info
```

---

## Deployment

The project includes:

* Graceful shutdown handling
* Environment-based configuration
* PM2 ecosystem configuration in prod/

---

## Key Learnings

* Designing scalable backend architecture
* Implementing filtering and pagination
* Applying security best practices
* Building observable systems with logging and tracing
* Using Redis queues for background processing
* Writing production-ready backend code

---
