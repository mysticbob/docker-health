# Docker Python Healthcheck

A demonstration project showing how to implement proper health checks for Python applications running in Docker containers.

## Overview

This project explores best practices for implementing health checks in Dockerized Python applications. Health checks are crucial for container orchestration systems to determine if a container is running properly and ready to serve requests.

## Features

- Implementation of Docker HEALTHCHECK instruction
- Python-based health check endpoints
- Examples of different health check strategies:
  - Basic HTTP endpoint checks
  - Database connection verification
  - Resource usage monitoring
  - Dependency service checks

## Getting Started

### Prerequisites

- Docker
- Python 3.8+
- Docker Compose (optional)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/docker-python-healthcheck
cd docker-python-healthcheck
```

2. Build the Docker image:

```bash
docker build -t python-healthcheck .
```

3. Create a data directory for the status file:

```bash
mkdir -p data
chmod 777 data
```

4. Start the container:

```bash
docker-compose up -d
```

5. Monitor the health status:

```bash
# Check container health status
docker ps
docker inspect --format='{{.State.Health.Status}}' python_healthcheck_app

# View container logs
docker logs python_healthcheck_app
```

## How It Works

The project demonstrates a simple health check implementation where:

1. The main application (`main.py`) randomly sets a status between 'good' and 'bad' every 10 seconds
2. The health check script (`health_check.py`) monitors this status file
3. Docker's HEALTHCHECK instruction runs the health check script every second
4. The container is considered:
   - Healthy when status is 'good'
   - Unhealthy when status is 'bad' or the status file is missing

## Configuration

The health check behavior can be modified through environment variables in the Dockerfile:

- `STATUS_FILE`: Location of the status file (default: /app/data/status.txt)
- `HEALTHCHECK_INTERVAL`: Time between checks (default: 1s)
- `HEALTHCHECK_TIMEOUT`: Maximum time for check (default: 5s)
- `HEALTHCHECK_RETRIES`: Number of retries before failing (default: 3)
- `HEALTHCHECK_START_PERIOD`: Initial grace period (default: 5s)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
