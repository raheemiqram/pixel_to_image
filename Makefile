SHELL=/bin/bash
.DEFAULT_GOAL := help


deploy:
	git pull
	pip install -r requirements/base.txt
	python manage.py migrate --no-input
	python manage.py collectstatic --no-input

pre-commit:
	pre-commit run --all-files

collectstatic:
	python3 manage.py collectstatic

runserver:
	python3 manage.py runserver

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

test:
	python3 manage.py test


load_test_data:
	 python3 manage.py test_data


run: makemigrations migrate load_test_data runserver