install:
	pip install pipreqs
	pipreqs . --force
	pip install -r requirements.txt
	pip install .

test:
	nosetests
