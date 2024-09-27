CONTAINER_NAME=docker-scalable-microservice-1
SERVICE_NAME=scalable-microservice
DOCKER_COMPOSE=docker-compose -f builder/docker/docker-compose.yml --env-file builder/.env

all: build up

build:
	@${DOCKER_COMPOSE} build --pull

up:
	@${DOCKER_COMPOSE} up

up-silent:
	@${DOCKER_COMPOSE} up -d

up-no-recreate:
	@${DOCKER_COMPOSE} up -d --no-recreate

down:
	@${DOCKER_COMPOSE} down

shell:
	@docker exec -it ${CONTAINER_NAME} bash

logs:
	${DOCKER_COMPOSE} logs -f

test: up-no-recreate
	${DOCKER_COMPOSE} run --rm ${SERVICE_NAME} pytest --disable-pytest-warnings tests/

test-file: up-no-recreate
	${DOCKER_COMPOSE} run --rm ${SERVICE_NAME} pytest --disable-pytest-warnings ${FILE}
