test:
	. venv/bin/activate
	./setup_tests.sh
	python3 -m pytest
