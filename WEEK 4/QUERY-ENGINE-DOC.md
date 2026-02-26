# Query Engine Documentation – Week 4 Day 3

## Overview

In Day 3, I implemented a dynamic and failure-safe Product API using a layered architecture approach:

Controller → Service → Repository → Database

The goal was to build a flexible query engine that supports:

- Text search
- Price filtering
- Tag filtering
- Sorting
- Pagination
- Soft delete
- Unified error handling

This API simulates a real-world production query system.

---

## Architecture Flow

1. Controller handles HTTP request and response.
2. Service layer contains business logic.
3. Repository handles database queries.
4. Error middleware formats all errors consistently.

This separation ensures clean and maintainable code.

---

## Dynamic Query System

The API supports flexible query parameters:

Example:

GET /products?search=phone&minPrice=100&maxPrice=500&sort=price:desc&tags=apple,samsung&page=1&limit=5

Supported filters:

- search → Full-text search on name and description
- minPrice / maxPrice → Price range filtering
- tags → Filter products by tags
- sort → Sorting format (field:asc/desc)
- page → Pagination page number
- limit → Number of items per page
- includeDeleted → Include soft-deleted records

The repository dynamically builds a MongoDB query object based on these parameters.

---

## Soft Delete Strategy

Instead of permanently deleting a product, we update:

deletedAt: Date

Normal queries automatically exclude deleted records.

If includeDeleted=true is passed, soft-deleted records are included.

This prevents permanent data loss and follows production best practices.

---

## Index Strategy

Indexes used:

- Compound index: { status: 1, createdAt: -1 }
- Text index on name and description

These indexes improve performance for filtering and sorting.

---

## Pagination Strategy

Pagination is implemented using:

skip = (page - 1) * limit

Response includes:

- data
- total
- page
- totalPages

This ensures scalable and structured responses.

---

## Error Handling

All errors are handled by a centralized middleware.

Error response format:

{
  "success": false,
  "message": "...",
  "code": "...",
  "timestamp": "...",
  "path": "..."
}

This ensures consistent and production-safe API behavior.

---

## Conclusion

This query engine demonstrates:

- Clean layered architecture
- Dynamic filter building
- Soft delete implementation
- Structured error handling
- Optimized database indexing

T
