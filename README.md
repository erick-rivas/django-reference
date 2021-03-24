# Django Reference

This repository holds the source code of a **reference** for the development of a **REST API with graphql support** based on Django framework

## Project structure

-   **/routes**: Api routes extensions (Custom endpoints definitions)
-   **/domain**: Business logic methods
-   **/models**: Model extensions
-   **/models/fixtures**: Initial data inserts (Eg. dummy data and catalogs)
-   /app/settings.py: Django settings
-   /seed: Autogenerated files produced by seed-builder: It includes model definitions, CRUD endpoint creation and graphql implementation

## Quickstart

-   Install [Python3](https://www.python.org/downloads/)
-   Install [PostgreSQL](https://www.postgresqltutorial.com/postgresql-getting-started/)
-   Clone this repository
    
-   Execute setup script `
```bash
./bin/setup.sh <DB_NAME> <DB_USER> <DB_PASSWORD>
```
>   *For windows, run the ./bin/setup.sh commands manually*

-   Optionally configure .env.dev fields with server attributes, database connections, secret keys, etc

-   Run server
```bash
python3 manage.py runserver
```

## Documentation

-   All documentation is in the `docs` directory or ìn http://localhost:8000 when server is running