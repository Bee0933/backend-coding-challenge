install:
	# install dependencies
	pip install --upgrade pip &&\
		pip install -r requirements.txt 
format:
	# format python code with black
	black *.py  app/*.py app/db/*.py app/endpoints/*.py
lint:
	# check code syntaxes
	pylint --disable=R,C *.py app/*.py app/db/*.py app/endpoints/*.py

populate:
	# populate json data in database
	chmod +x populate.py &&\
		./ populate.py --json_filename planning.json

run:
	# run application 
	python3 app/main.py

all: install format lint populate run 