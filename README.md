# Django API

This repository holds the source code of a **reference** for the development of a **Django api** written mainly in python.

## Architecture design

The reference uses a architecure based on a Generic Model View pattern, Inspired by the architecture of [Django framework](https://www.djangoproject.com) and [Django REST framework](https://www.django-rest-framework.org)

### General description

In general terms, the architecture uses the following structure:

  - /app: App general settings
    - api.py: Api routes definitions
    - settings.py: App settings (dependencies, configurations, etc)
  - /models: Model definitions [More info](https://docs.djangoproject.com/en/2.1/topics/db/models/)
  - /serializers: Model serializers [More info](https://www.django-rest-framework.org/api-guide/serializers/)
  - /views: Api views [More info](https://www.django-rest-framework.org/api-guide/views/)

## Pre-requisites:

 * Download & install [Python3](https://www.python.org/downloads/)
 * Download & install [PyCharm CE](https://www.jetbrains.com/pycharm/download/)

### To start coding and build:

 * Clone this repository.
 * Install postgresql database.
 * Create virtual environment
  ```bash
 $ python3 -m venv .env
 $ . env/bin/activate
 ```
 * Open project in PyCharm
 * Go to PyCharm > Preferences > Project interpreter > Add > Select <project_dir>/venv
 * Install dependencies (Suggested in PyCharm Terminal)
 ```bash
(.env)$ pip3 install -r requirements.txt
 ```
 * Set database settings in app/settings.py
 * Create a new database with the name shown in the last step
 * Make migrations
 ```bash
(.env)$ python3 manage.py makemigrations
 ```
 * Run migrations
 ```bash
(.env)$ python3 manage.py migrate
 ```
 * Run project
```bash
(.env)$ python3 manage.py runserver
 ```

 ### To enable admin panel

 * Add models to /app/admin
 * Create superuser
 ```bash
(.env)$ python3 manage.py createsuperuser
 ```
 * Open admin panel 
 ```bash
 http://localhost:8080/admin
 ```

### Examples

 * Example docs.
 ```bash
 http://localhost:8080/docs
 ```
  * Example requests. 
 ```bash
 GET http://localhost:8080/v1/players
 ```

 
 