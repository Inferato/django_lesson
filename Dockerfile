FROM python:3.12-slim


RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /django_app

COPY ./test_project /django_app/test_project

RUN pip install --no-cache-dir -r  /django_app/test_project/requirements.txt

WORKDIR /django_app/test_project

EXPOSE 8000