start: migrate populate_db run_server

migrate:
	python manage.py makemigrations
	python manage.py migrate

run_server:
	python manage.py runserver 0.0.0.0:8000

tests:
	python manage.py test
	
populate_db:
	python manage.py load_data