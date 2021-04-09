# Django Reference

This repository holds a **reference** for the development of a **REST API with graphql support** based on Django framework

## Quickstart

-   Install [Docker Engine](https://docs.docker.com/engine/install/) & [Compose](https://docs.docker.com/compose/install/)
    >   For linux installation adjust docker permissions [guide](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
-   Clone this repository
-   Set execute permissions to script (linux) `chmod +x bin/setup.sh`
-   Execute setup script `bin/setup.sh` (For windows `bin/setup.bat`)
-   Run server with `bin/start.sh` (For windows `bin/start.bat`)
    -   To show server logs execute `bin/logs.sh` (For windows `bin/logs.bat`)
    -   To stop server execute `bin/stop.sh` (For windows `bin/stop.bat`)

### Examples

-   API browser: [http://localhost:8008/api](http://localhost:8008/api)
-   Graphql browser: [http://localhost:8008/graphql](http://localhost:8008/graphql)
-   Admin pane: [http://localhost:8008/admin](http://localhost:8008/admin)
    >   user:admin@email.com, pass: 123
    
## Documentation

-   All documentation is in the `docs` directory