# Containerized Host Resource Monitor (CLI)

Lightweight, containerised system monitor (CPU/Memory) run from a Docker environment.

Solves the "container isolation paradox" by PID namespace sharing (`--pid=host`) to allow a Docker container to monitor the underlying host operating system.

## Features
* **Live Dashboard:** Real-time CPU and Memory visualization using Python `psutil`.
* **Zero-Dependency Host:** Runs on any machine with Docker installed; no Python/pip required on the host.
* **Session Analytics:** detailed summary (Avg/Max peaks) upon exit (`Ctrl+C`).
* **Orchestration:** Self-healing Bash script (`run.sh`) that handles image building and container lifecycle.

## Tech Stack
* **Python 3.11 (Slim)**
* **Docker** 
* **Bash** 

## Quick Start
No installation required other than Docker.

```bash
# Clone the repository
git clone "https://github.com/Minimaruva/Simple-Resource-Monitor"
cd Simple-Resource-Monitor

# Make the script executable
chmod +x run.sh

# Run the monitor
./run.sh
