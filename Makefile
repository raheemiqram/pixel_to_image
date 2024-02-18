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
	python manage.py collectstatic

runserver:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

test:
	python manage.py test


load_test_data:
	 python manage.py test_data


run: makemigrations migrate load_test_data runserver