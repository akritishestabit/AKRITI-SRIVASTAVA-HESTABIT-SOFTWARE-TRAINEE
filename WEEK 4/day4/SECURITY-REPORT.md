# WEEK 4 – DAY 4  
## Security Hardening & Vulnerability Testing Report

---

## Objective

The goal of Day 4 was to secure the Product API by reducing attack surface and enforcing strict input control. The API was tested against common web vulnerabilities and hardened using middleware and validation layers.

---

## Implemented Security Measures

- Helmet for secure HTTP headers
- Rate limiting (100 requests per 15 minutes per IP)
- Body size limit (10kb)
- HTTP Parameter Pollution (HPP) protection
- Centralized Joi validation middleware
- Payload whitelisting using stripUnknown
- Soft delete protection
- Structured error handling

---

## Tested Vulnerabilities & Results

### 1. Invalid Payload Injection

**Test Performed:**
POST /products with incomplete fields.

**Result:**
API returned 400 VALIDATION_ERROR.
No product was stored in database.

---

### 2. Unknown Field Injection

**Test Performed:**
Sent additional unexpected field in request body.

**Result:**
Request succeeded but unknown field was automatically removed.
Database did not store malicious field.

This confirms payload whitelisting is active.

---

### 3. HTTP Parameter Pollution

**Test Performed:**
GET /products?price=100&price=200

**Result:**
Duplicate parameters were sanitized.
No crash or unexpected behavior occurred.

---

### 4. Rate Limiting (Request Flooding Test)

**Test Performed:**
Sent more than 100 requests within 15 minutes.

**Result:**
API returned rate limit error message.
Further requests were blocked temporarily.

---

### 5. Large Payload Attack

**Test Performed:**
Sent JSON body larger than 10kb.

**Result:**
Request rejected with payload size error.
Server memory remained protected.

---

### 6. Soft Delete Protection

**Test Performed:**
Deleted product and attempted to access it again.

**Result:**
API returned PRODUCT_NOT_FOUND.
Soft-deleted records are excluded from queries.

---

## Conclusion

The API is now hardened against:

- Invalid data injection
- Parameter pollution attacks
- Request flooding
- Oversized payload abuse
- Unauthorized access to deleted records

The backend follows layered security architecture and enforces strict input validation before business logic execution.

The system is secure from a baseline production perspective.