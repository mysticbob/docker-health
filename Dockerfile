# Dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app

# Create application directory and data directory
WORKDIR $APP_HOME
RUN mkdir -p ${APP_HOME}/data && chmod 777 ${APP_HOME}/data

# Copy application scripts
COPY main.py health_check.py ${APP_HOME}/

# Install any dependencies (none needed for this example)
# RUN pip install --no-cache-dir <your-dependencies>

# Set execute permissions for the scripts
RUN chmod +x main.py health_check.py

# Set the working directory for the status file
ENV STATUS_FILE=${APP_HOME}/data/status.txt

# Define the health check
HEALTHCHECK --interval=1s --timeout=5s --start-period=5s --retries=3 \
  CMD ["python", "health_check.py"]

# Start the main application
CMD ["python", "main.py"]
