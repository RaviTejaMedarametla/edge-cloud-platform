#!/bin/bash
set -e

echo "Setting up the development environment..."

# Build and start all services
if [ -f docker-compose.yml ]; then
    docker-compose pull
    docker-compose build
    docker-compose up -d
fi

echo "Setup complete."
