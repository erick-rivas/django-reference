# Django API - Deployment Docker

This file contains guides to run and deploy this application with Docker.

Commands shall be ran as administrator or superuser to avoid permission issues. 

To get an overview of the usage of Docker refer to this [guide](https://docs.docker.com/get-started/overview/)

## Docker installation

Follow the installation process for your OS from the [official docker documentation](https://docs.docker.com/get-docker/)

### For MacOS Users

Follow the installation process from the [official documentation](https://docs.docker.com/docker-for-mac/install/)

### For Windows users

Follow the installation profess from the [official documentation](https://docs.docker.com/docker-for-windows/install/)

### For Ubuntu users

First, update your existing list of packages:

```
sudo apt update
```

Next, install a few prerequisite packages which let apt use packages over HTTPS:

```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

Then add the GPG key for the official Docker repository to your system:

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Add the Docker repository to APT sources:

```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
```

Next, update the package database with the Docker packages from the newly added repo:

```
sudo apt update
```

Finally, install Docker:

```
sudo apt install docker-ce
```

## For development

Copy the `.env.example` file as `.env.dev`.

```
cp .env.example .env.dev #Linux / MacOS
copy .env.example .env.dev #Windows
```
Change the following atributes to develop in a Docker container:

```
#For docker development
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DB_HOST=db # Delete comment in this line

#docker-compose.yml variables
POSTGRES_DB=django_db #POSTGRES_DB name must be the same as in DB_NAME
POSTGRES_USER=django_db #POSTGRES_USER name must be the same as in DB_USER
POSTGRES_PASSWORD=n0m3l0 #POSTGRES_PASSWORD name must be the same as in DB_PASSWORD
DATABASE=postgres
```

Next run the next command from the root directory of the project as **administrator or superuser**:

```
docker-compose up -d --build
```
