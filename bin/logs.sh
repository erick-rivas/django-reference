#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

sudo docker-compose -f bin/docker/docker-compose.yml logs --follow --tail 250 django_reference_django django_reference_celery