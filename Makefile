IMAGE_NAME = "visitor-badge"

.PHONY: build lint

build:
	python bin/sync_ignore.py
	@echo "Build Dockerfile"
	docker build -t $(IMAGE_NAME) .

lint:
	docker run --rm --volume $(CURDIR):/app --workdir /app pyfound/black:latest_release black .