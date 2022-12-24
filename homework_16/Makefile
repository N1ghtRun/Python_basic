req:
	pip install -r requirements.txt

tests:
	flake8 --ignore=E501 main.py
	mypy main.py

run: tests
	python main.py
