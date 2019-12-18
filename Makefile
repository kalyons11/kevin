default: install test

install:
	pip install -r requirements.txt
	pip install . --upgrade

test:
	nosetests --with-doctest --nocapture

lint:
	pylint kevin

deploy:
	pip install pipreqs
	pipreqs . --force
