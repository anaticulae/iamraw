.PHONY: docker-build docker-run build clean

VERSION := $(shell git rev-parse --short HEAD 2>/dev/null || echo "latest")
CURDIR := $(CURDIR)

NAME = iamraw
IMAGE := $(NAME):$(VERSION)
IMAGE_NAME := ghcr.io/anaticulae/$(IMAGE)

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-upload:
	docker push $(IMAGE_NAME)

docker-doctest: docker-build
	docker run\
		-v $(CURDIR):/var/workdir\
		$(IMAGE_NAME)\
		"baw test docs"

docker-fasttest: docker-decrypt
	docker run\
		-v $(CURDIR):/var/workdir\
		-v /tmp/power:/tmp/power\
		$(IMAGE_NAME)\
		"baw test fast"

docker-longtest: docker-decrypt
	docker run\
		-v $(CURDIR):/var/workdir\
		-v /tmp/power:/tmp/power\
		$(IMAGE_NAME)\
		"baw test long"

docker-alltest: docker-decrypt
	docker run\
		-v $(CURDIR):/var/workdir\
		-v /tmp/power:/tmp/power\
		$(IMAGE_NAME)\
		"baw test all"

docker-lint: docker-build
	docker run\
		-v $(CURDIR):/var/workdir\
		$(IMAGE_NAME)\
		"baw lint all"

docker-decrypt: docker-build
	docker run\
		-v $(CURDIR):/var/workdir\
		-v /tmp/power:/tmp/power\
		-e HOVERPOWER_STORE=/var/workdir/hoverpower/repo\
		-e HOVERPOWER_SECRET=$(HOVERPOWER_SECRET)\
		$(IMAGE_NAME)\
		"powerdownload && powerdecrypt"

docker-release: docker-build
	docker run\
		-v $(CURDIR):/var/workdir\
		-e GH_TOKEN=$(GH_TOKEN)\
		$(IMAGE_NAME)\
		"baw release --no_test --no_linter"
