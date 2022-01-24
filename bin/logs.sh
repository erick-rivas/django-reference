#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

sudo docker-compose -f bin/docker/docker-compose-dev.yml logs --follow --tail 100 django_reference_django