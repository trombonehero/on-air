all: app

app:
	python setup.py py2app

dev: requirements.txt

install: app
	mv dist/On\ Air.app ~/Applications

requirements.txt: requirements.in
	pip-compile requirements.in > requirements.txt
