install:
	poetry install

check: install
	poetry run prospector

build:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	docker build -t nekonyuu/movies-view-injector .

start:
	poetry run faust -A website_events worker -l info