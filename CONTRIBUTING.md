# Python hebrew numbers

## Contribution guidelines

### quickstart
* clone the repo
* create a python virtualenv
* change into the repo directory
* activate the virtualenv
```bash
(venv) python-hebrew-numbers$ pip install -e .
(venv) python-hebrew-numbers$ python -m hebrew_numbers.tests
```

## Publishing to pypi

increment the version in VERSION.txt

```
rm -rf dist build &&\
python3 setup.py sdist bdist_wheel --universal &&\
twine upload dist/*
```
