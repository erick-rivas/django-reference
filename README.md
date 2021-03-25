# Django Reference

This repository holds the source code of a **reference** for the development of a **REST API with graphql support** based on Django framework

## Project structure

-   **/routes**: Api routes extensions (Custom endpoints definitions)
-   **/domain**: Business logic methods
-   **/models**: Data models extensions
-   **/models/fixtures**: Initial data inserts (Eg. dummy data and catalogs)
-   /app/settings.py: Django settings
-   /seed: Autogenerated files produced by [seed-builder](./docs/060_seed_builder.md)

## Quickstart

-   Install [Docker Engine](https://docs.docker.com/engine/install/)
-   Install [Docker Compose](https://docs.docker.com/compose/install/)
-   Clone this repository
-   Set execute permissions to scripts (linux) `chmod +x bin/*`
-   Execute setup script `bin/setup`
    >   For linux is necessary to execute commands as root (e.g. sudo bin/setup)

-   Open server [http://localhost:8000](http://localhost:8000)

## Documentation

-   All documentation is in the `docs` directory