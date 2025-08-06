# Django reference

This repository holds a **reference** for the development of a **REST API with graphql support** based on Django framework

## Quickstart

-   Install [Docker Engine 28.3.x or Desktop 4.43.x](https://docs.docker.com/engine/install/)
-   Install [Python 3.11.x](https://www.python.org/downloads/)
-   Clone this repository
-   Execute setup script `bin/setup`
    >  For unix systems execute shell files `*.sh` (without sudo) and for windows batch `.bat` (e.g `bin/setup.sh` or `bin/setup.bat`)
-   Start server with `bin/start`

### Examples

-   Admin pane: [http://localhost:8008/admin](http://localhost:8008/admin)
-   API browser: [http://localhost:8008/api](http://localhost:8008/api)
-   Graphql browser: [http://localhost:8008/graphql](http://localhost:8008/graphql)

## Documentation

-   All documentation is in the [docs](docs) directory

### Seed documentation

-   [General](docs/seed/010_general.md)
-   [Routes](docs/seed/020_routes.md)
-   [Domain](docs/seed/030_domain.md)
-   [Models](docs/seed/040_models.md)
-   [Seed builder](docs/seed/110_seed_builder.md)
-   [Seed commons](docs/seed/120_seed_commons.md)
-   [Deploy - Ubuntu](docs/seed/210_deploy_ubuntu.md)