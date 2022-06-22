start: migrate populate_db run_server

migrate:
	python manage.py makemigrations
	python manage.py migrate

run_server:
	python manage.py runserver 0.0.0.0:8000

tests:
	python manage.py test
	
populate_db: download_data
	python manage.py load_data

download_data:
	curl https://api.datos.gob.mx/v1/precio.gasolina.publico?pageSize=100000  --output data.json
	sed -i 's/﻿permisoid/permisoid/g' ./data.json
	sed -i 's/:""/:null/g' ./data.json
	sed -i 's/_id/id/g' ./data.json
	sed -i 's/|",/",/g' ./data.json