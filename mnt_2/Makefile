setup:
	pip install -r requirements.txt
	flake8 --ignore=E501 main.py
	mypy main.py
	pytest

run: setup
	python main.py
