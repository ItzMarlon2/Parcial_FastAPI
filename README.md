# PARCIAL 1 - ELECTIVA 3 - MARLON CAMPO 

This project contains a basic CRUD between two entities with their respective validations, using docker to create the database in postgresQL.

## Requirements

- Docker
- Docker Compose

## Initial Setup

1. Clone the repository: https://github.com/ItzMarlon2/Parcial_FastAPI.git
2. Navigate to the project directory: cd parcial-1

## Running with Docker Compose

To start the services with Docker Compose, run:

```bash
docker-compose up -d
```

This will bring up two services:
- **postgres**: PostgreSQL database.
- **fastapi**: FastAPI application accessible at `http://localhost:5000`.

## Stopping the Services

To stop and remove the containers, use:


```bash
docker-compose down
```

## Directory Structure
Provide a brief description of the most important directory structure, for example:

```bash
/alembic
    /env.py
/app
    /config
    /models
    /schemas
    /services
    /repositories
    /routes
    main.py
/
    Dockerfile
    docker-compose.yml
```


