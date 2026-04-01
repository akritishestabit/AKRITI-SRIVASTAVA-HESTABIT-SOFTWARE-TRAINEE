# Base image
FROM python:3.12-slim

# Working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run API
CMD ["uvicorn", "deployment.api:app", "--host", "0.0.0.0", "--port", "8000"]