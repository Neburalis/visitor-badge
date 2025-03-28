IMAGE_NAME = "visitor-badge"

.PHONY: build lint

build:
	python bin/sync_ignore.py
	@echo "Build Dockerfile"
	docker compose build

lint:
	docker run --rm --volume $(CURDIR):/app --workdir /app pyfound/black:latest_release black .

run:
	docker compose up -d

stop:
	docker compose down

logs:
	docker compose logs -f