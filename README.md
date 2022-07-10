# Django reference

This repository holds a **reference** for the development of a **REST API with graphql support** based on Django framework

## Quickstart

-   Install [Python 3.8.x](https://www.python.org/downloads/)
-   Install [Docker Desktop 4.10.x](https://docs.docker.com/desktop/)
-   Clone this repository
-   Execute setup script `bin/setup`
    -   For unix systems execute shell file `*.sh` and for windows batch `.bat` (e.g `bin/setup.sh` or `bin/setup.bat`)
    >   Warning: Don't execute any script with sudo
-   Start server with `bin/start`
    -   To run server in foreground execute `bin/run`

### Examples

-   Admin pane: [http://localhost:8008/admin](http://localhost:8008/admin)
    >   user:admin@email.com, pass: 123
-   API browser: [http://localhost:8008/api](http://localhost:8008/api)
-   Graphql browser: [http://localhost:8008/graphql](http://localhost:8008/graphql)

## Documentation

-   All documentation is in the [docs](./seed/docs/010_general.md) directory and in the server path [http://localhost:8008/docs](http://localhost:8008/docs)