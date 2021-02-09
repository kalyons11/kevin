default: install test

install:
	pip install -r requirements.txt
	pip install . --upgrade

test:
	nosetests --with-doctest --nocapture
	cd kevin/tests; chmod +x run_cpp_tests.sh; ./run_cpp_tests.sh

lint:
	pylint kevin

deploy:
	pip install pipreqs
	pipreqs . --force
