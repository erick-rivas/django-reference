FROM python:3.8.3-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip==21.0.1
RUN apk update && apk add postgresql-dev postgresql-client gcc python3-dev musl-dev git 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .