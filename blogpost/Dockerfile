FROM python:3.12-slim


RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./blogpost /app/blogpost

RUN pip install --no-cache-dir -r  /app/blogpost/requirements.txt

WORKDIR /app/blogpost

EXPOSE 9000