# to_deploy app

## Running

We have several steps to be runned: preparations and the container itself.

### Preparations

1. `docker-compose run web psql postgres -U postgres --host=db --port=5432 -c "create database to_deploy;"`
2. `docker-compose run web python manage.py migrate`

### Running container

To be able to access your application from browser run:

1. `docker-compose up`

### Extra commands

To create superuser:

1. `docker-compose run web python manage.py createsuperuser`
