all: app

app:
	python setup.py py2app

dev: requirements.txt

requirements.txt: requirements.in
	pip-compile requirements.in > requirements.txt
