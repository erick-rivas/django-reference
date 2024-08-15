### __Seed builder__
#   Autogenerated Dockerfile
#   Add custom commands at the end

FROM python:3.8.18
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip==24.2
RUN apt update
RUN apt install -y gcc postgresql-client python3-dev build-essential software-properties-common yarn \
        libssl-dev libreadline-dev libyaml-dev libxml2-dev libxslt1-dev libcurl4-openssl-dev  libffi-dev zlib1g-dev
ENV TZ=America/Mexico_City

# __End autogenerated__
# Include commands after this block
###

COPY requirements.txt .
COPY seed/requirements.txt seed/
RUN pip install -r requirements.txt --no-cache-dir
COPY . .