#!/bin/bash

echo "Starting production deployment..."

docker compose -f docker-compose.prod.yml up -d --build

echo "Deployment finished"