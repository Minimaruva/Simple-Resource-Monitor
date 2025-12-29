FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy the monitoring script
COPY monitor.py .

# Install dependencies
RUN pip install psutil

# CMD to run the script
CMD ["python", "monitor.py"]