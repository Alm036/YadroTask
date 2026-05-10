FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY script.py .

CMD ["python3", "script.py"]
