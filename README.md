# Django API

This repository holds the source code of a **reference** for the development of a **Django api** written mainly in typescript.

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