# Linux Inside Docker Container – Observations

## 1. Base Image
- node:18-alpine
- Lightweight Alpine Linux distribution

## 2. Running User
- Container runs as: root
- UID: 0
- Production best practice: Avoid running as root

## 3. Process Model
- Node process runs as PID 1
- PID 1 is main container process
- If PID 1 exits, container stops

## 4. Filesystem Structure
- /app contains application code
- /.dockerenv confirms containerized environment
- Minimal Linux filesystem present

## 5. Storage
- Overlay filesystem used
- Shares host storage
- Not a full VM disk

## 6. Logs
- Logs printed to STDOUT
- Accessible via docker logs
- Best practice: log to STDOUT in containers

## 7. Learnings
- Container is lightweight
- Shares host kernel
- Runs as isolated Linux process
- Not a virtual machine