FROM python:3.8.3-alpine
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip==21.0.1
RUN apk update && apk add gcc postgresql-dev postgresql-client python3-dev musl-dev openssh-client
COPY requirements.txt .
COPY seed/requirements.txt seed/
RUN pip install -r requirements.txt
COPY . .