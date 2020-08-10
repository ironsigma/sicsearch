test:
	py.test tests

pypi: clean test
	python3 setup.py sdist
	python3 setup.py bdist_wheel

pypi-upload:
	twine upload dist/*

venv:
	python3 -m venv venv

init-venv:
	pip install --upgrade pip
	pip install -r requirements.txt

clean:
	rm -rf build/ dist/ sicsearch.egg-info
	find . -name .pytest_cache -o -name __pycache__ -exec rm -r "{}" +
	find . -name '*.pyc' -exec rm "{}" +
