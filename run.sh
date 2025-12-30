#!/bin/bash

IMAGE_NAME="system-monitor"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed"
    exit 1
fi

# Build image
# -q checks if the image ID exists. If not, we build.
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
    echo "Building Docker image"
    docker build -t $IMAGE_NAME .
else
    echo "Image '$IMAGE_NAME' already exists. Skipping build."
fi

# Run the container
echo "Starting Monitor... (Press Ctrl+C to stop)"
echo "------------------------------------------"

# --rm: Automatically remove the container when it exits (saves disk space)
# -it: Interactive terminal (allows you to see the output)
# --pid=host: - allows reading host metrics
docker run --rm -it --pid=host $IMAGE_NAME