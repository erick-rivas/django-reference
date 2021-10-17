# Django reference

This repository holds a **reference** for the development of a **REST API with graphql support** based on Django framework

## Quickstart

-   Install [Python 3.6+](https://www.python.org/downloads/)
-   Install [Docker Engine 20.10+](https://docs.docker.com/engine/install/) & [Compose 1.28.5+](https://docs.docker.com/compose/install/)
-   Clone this repository
-   Execute setup script `bin/setup.sh` (For windows `bin/setup.bat`)
    >   Warning: Don't run any script with sudo
-   Run server with `bin/start.sh` (For windows `bin/start.bat`)
    -   To show server logs execute `bin/logs.sh` (For windows `bin/logs.bat`)
    -   To stop server execute `bin/stop.sh` (For windows `bin/stop.bat`)

### Examples

-   API browser: [http://localhost:8008/api](http://localhost:8008/api)
-   Graphql browser: [http://localhost:8008/graphql](http://localhost:8008/graphql)
-   Admin pane: [http://localhost:8008/admin](http://localhost:8008/admin)
    >   user:admin@email.com, pass: 123

## Documentation

-   All documentation is in the [docs](./docs/010_general.md) directory and in the server path [http://localhost:8008/docs](http://localhost:8008/docs)