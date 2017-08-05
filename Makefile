default:
	install test

install:
	pip install -r requirements.txt
	pip install .

test:
	nosetests

deploy:
	pip install pipreqs
	pipreqs . --force
