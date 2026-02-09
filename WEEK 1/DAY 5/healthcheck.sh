#!/bin/bash

# Cron-safe PATH
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

BASE_DIR="/home/akritisrivastava/Desktop/AKRITI-SRIVASTAVA-HESTABIT-SOFTWARE-TRAINEE/WEEK 1/DAY 5"
SERVER_URL="http://localhost:3000"

LOG_FILE="$BASE_DIR/logs/health.log"
DEBUG_LOG="$BASE_DIR/logs/cron-debug.log"

# Proof cron triggered
echo "$(date) : Cron triggered" >> "$DEBUG_LOG"

# Health check with timeout (IMPORTANT)
if /usr/bin/curl --max-time 5 -s --head "$SERVER_URL" > /dev/null; then
  echo "$(date) : Server UP at $SERVER_URL" >> "$LOG_FILE"
else
  echo "$(date) : Server DOWN at $SERVER_URL" >> "$LOG_FILE"
fi


