FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY src/monitor.py .

RUN pip install --no-cache-dir psutil

CMD ["python", "monitor.py"]