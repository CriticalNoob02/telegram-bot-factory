NAME ?= teste

create-venv:
	virtualenv -p /usr/bin/python3.10 .venv

install:
	pip install -r requirements.txt

gen:
	python3 scripts/gen_command.py ${NAME}

run:
	python3 app/run.py

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
