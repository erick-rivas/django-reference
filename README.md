# Django reference

This repository holds a **reference** for the development of a **REST API with graphql support** based on Django framework

## Quickstart

-   Install [Python 3.8.x](https://www.python.org/downloads/)
-   Install [Docker Desktop 4.22.x](https://docs.docker.com/desktop/)
-   Clone this repository
-   Execute setup script `bin/setup`
    >  For unix systems execute shell file `*.sh` (without sudo) and for windows batch `.bat` (e.g `bin/setup.sh` or `bin/setup.bat`)
-   Start server with `bin/start`

### Examples

-   Admin pane: [http://localhost:8008/admin](http://localhost:8008/admin)
    >   user:admin@email.com
-   API browser: [http://localhost:8008/api](http://localhost:8008/api)
-   Graphql browser: [http://localhost:8008/graphql](http://localhost:8008/graphql)

## Documentation

-   All documentation is in the [docs](seed/docs) directory

### Index

-   [Development](seed/docs/010_general.md)
-   [Routes](seed/docs/020_routes.md)
-   [Domain](seed/docs/030_domain.md)
-   [Models](seed/docs/040_models.md)
-   [Seed builder](seed/docs/110_seed_builder.md)
-   [Seed commons](seed/docs/120_seed_commons.md)
-   [Deploy - Ubuntu](seed/docs/210_deploy_ubuntu.md)