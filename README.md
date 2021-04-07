# Django Reference

This repository holds a **reference** for the development of a **REST API with graphql support** based on Django framework

## Quickstart

-   Install [Docker Engine](https://docs.docker.com/engine/install/) & [Compose](https://docs.docker.com/compose/install/)
    >   For linux adjust docker for non-root user usage [guide](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
-   Clone this repository
-   Set execute permissions to scripts (linux) `chmod +x bin/setup`
-   Execute setup script `bin/setup`, for windows `bin/setup.bat`
-   Run server `bin/start`

### Examples

-   API browser: [http://localhost:8008/api](http://localhost:8008/api)
-   Graphql browser: [http://localhost:8008/graphql](http://localhost:8008/graphql)
-   Admin pane: [http://localhost:8008/admin](http://localhost:8008/admin)
    >   user:admin@email.com, pass: 123
    
## Documentation

-   All documentation is in the `docs` directory