# Registry where you want store your Docker images
DOCKER_REGISTRY = cr.msk.sbercloud.ru/577618d7-0b37-452d-9a1a-4f0ad7a84d10
PORTS = 8080:8080
PROJECT_NAME = deploy-test

REPO_PATH := $(shell git rev-parse --show-toplevel)
CHANGED_FILES := $(shell git diff-files)

ifeq ($(strip $(CHANGED_FILES)),)
	GIT_VERSION := $(shell git describe --tags --long --always)
else
	GIT_VERSION := $(shell git describe --tags --long --always)-dirty-$(shell git diff | shasum -a256 | cut -c -6)
endif

IMG ?= ${DOCKER_REGISTRY}/${PROJECT_NAME}
TAG ?= $(GIT_VERSION)

lock:
	poetry lock

linter:
	PYTHONPATH=$(shell pwd)/project poetry run black --line-length 120 .

# pre production
build:
	docker build -t ${IMG}:${TAG} .

run: build
	docker run -it -p ${PORTS} --rm --env-file .env ${IMG}:${TAG}

push: linter lock build
	docker push ${IMG}:${TAG}
