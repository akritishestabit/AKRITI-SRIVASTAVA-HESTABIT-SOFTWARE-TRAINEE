# Deployment Notes

## Requirements
- Node.js v18+
- MongoDB running
- Redis running

## Install Dependencies
npm install

## Start Development
npm run dev

## Start Production (PM2)
pm2 start prod/ecosystem.config.js

## Redis
Ensure Redis is running:
redis-server

## Logs
Application logs:
src/logs/combined.log
src/logs/error.log