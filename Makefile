default: install test

install:
	pip install -r requirements.txt
	pip install . --upgrade

test:
	nosetests --with-doctest --nocapture

deploy:
	pip install pipreqs
	pipreqs . --force
