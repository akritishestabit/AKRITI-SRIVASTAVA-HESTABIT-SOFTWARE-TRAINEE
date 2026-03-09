# SSL Setup with Docker and Nginx

In this exercise we configured HTTPS using a self-signed SSL certificate.

Steps:
1. Generated SSL certificate using OpenSSL.
2. Configured Nginx as reverse proxy.
3. Enabled HTTPS on port 443.
4. Connected Nginx to multiple backend containers.

Now requests go to Nginx and it forwards them to backend containers securely.