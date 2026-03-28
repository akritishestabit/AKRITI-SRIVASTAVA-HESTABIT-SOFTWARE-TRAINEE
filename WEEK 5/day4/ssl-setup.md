# SSL Setup using NGINX + mkcert

## Goal
Enable HTTPS locally using NGINX reverse proxy with self-signed certificates.

---

## Setup Steps

1. Install mkcert  
mkcert -install  

2. Generate certificate  
mkcert localhost  

This creates:
- localhost.pem  
- localhost-key.pem  

Place them in: nginx/certs/

---

## NGINX Config (SSL)

- HTTP server redirects to HTTPS  
- HTTPS server uses SSL certs  
- Requests are forwarded to backend containers  

---

## Docker Compose

- backend1 and backend2 run Node app  
- nginx acts as reverse proxy  
- ports expose HTTP and HTTPS  
- volumes mount config and certificates  

---

## Volumes Used

- nginx.conf → replaces default config  
- certs → provides SSL files inside container  

---

## Flow

1. User → http request  
2. NGINX → redirect to HTTPS  
3. Browser → secure connection (SSL)  
4. NGINX → decrypt request  
5. Forward → backend1/backend2  
6. Response → encrypted → browser  

---

## Key Points

- NGINX handles SSL (backend stays HTTP)  
- mkcert creates trusted local certificates  
- Use explicit port in redirect for custom ports  
- Volumes are required for SSL to work  

---

## Summary

NGINX + mkcert enables secure local development with HTTPS, reverse proxy, and load balancing.