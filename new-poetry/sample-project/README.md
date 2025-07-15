pip install coverage
poetry add --dev coverage
coverage run -m pytest
coverage report