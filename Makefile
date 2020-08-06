init:
	pip install -r requirements.txt

test:
	py.test tests

.PHONY: init test clean

clean:
	find . -name .pytest_cache -o -name __pycache__ -exec rm -r "{}" +
	find . -name '*.pyc' -exec rm "{}" +
