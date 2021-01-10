# For development

- [For development](#for-development)
  - [Run the container](#run-the-container)
  - [Troubleshooting](#troubleshooting)
  - [Executing commands on the Docker Container](#executing-commands-on-the-docker-container)
    - [Using fixtures](#using-fixtures)
    - [Inspecting the database](#inspecting-the-database)

## Run the container

Copy the `.env.example` file as `.env.dev`.

```
cp .env.example .env.dev #Linux / MacOS
copy .env.example .env.dev #Windows
```

Change the following atributes to develop in a Docker container:

1. Delete the comment on the `DB_HOST` line under the `#For docker development` section.
2. Add the values for the variables `POSTGRES_DB`, `POSTGRES_USER` and `POSTGRES_PASSWORD` with the same values from the `DB_NAME`, `DB_USER` and `DB_PASSWORD` values, for example:

```
#For docker development
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DB_HOST=db

#docker-compose.yml variables
POSTGRES_DB=django_db
POSTGRES_USER=django_db
POSTGRES_PASSWORD=n0m3l0
```

Inside `app/settings.py` remove the comment in the line:

```
# For Docker development, change the allowed hosts
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
```

Copy the files in the `bin/docker/config/development` folder to the root directory. Run the following command from the root directory:

```
cp -a bin/docker/config/development/. ./ #Linux & MacOS
xcopy /s bin\docker\config\development\. .\ #Windows
```

Or just copy the files with the file manager.

Next run the next command from the root directory of the project as **administrator or superuser**:

```
docker-compose --env-file ./.env.dev -f docker-compose.yml up -d --build
```

To check all the running containers in your system, use

```
docker ps -a #or
docker-compose ps
```

To stop a container use

```
docker stop [CONTAINER_ID]
```

To remove the volumes and the containers use

```
docker-compose down -v
```

To edit code live from a container see [the VSCode documentation](https://code.visualstudio.com/docs/remote/containers)

## Troubleshooting

If you are presented with an _standard_init_linux.go:[number]: exec user process caused “no such file or directory” - Docker_ error, open the **entrypoint.sh** file in Notepad++, go to _EDIT-> EOL conversion -> change from CRLF to LF_ and run the `docker-compose` again

If the `localhost:8000` is not connected run:

```
docker-compose --env-file ./.env.dev -f docker-compose.yml up --build
```

If you're presented with the following error:

```
django.db.utils.OperationalError: could not connect to server: Connection refused
    Is the server running on host "127.0.0.1" and accepting
    TCP/IP connections on port 5432?
```

try the following:

1. Inspect and kill any process that is running on port **5432** on your system
2. Make sure you deleted the comment on the line `DB_HOST=db` on the _.env.dev_ file

## Executing commands on the Docker Container

To execute a command on the docker container use the `exec` command [see the Docker documentation](https://docs.docker.com/engine/reference/commandline/exec/)

### Using fixtures

After starting the container, run the _exec_ command:

`docker-compose exec django python manage.py loaddata fixtures/*.yaml`

### Inspecting the database

To use _PSQL_ commands in the container access it by:

`docker-compose exec db psql --username=django_db --dbname=django_db`

or

`docker-compose exec db psql -U django_db`

And you'll be prompted with the _psql_ interface for the database in the container.