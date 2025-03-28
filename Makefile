IMAGE_NAME = "visitor-badge"

.PHONY: build lint

build:
	docker compose build

sync_ignore:
	python bin/sync_ignore.py

lint:
	docker run --rm --volume $(CURDIR):/app --workdir /app pyfound/black:latest_release black .

run:
	docker compose up -d

stop:
	docker compose down

logs:
	docker compose logs -f