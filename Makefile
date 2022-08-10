build:
	@python -m PyInstaller --onefile code_clinic.py

clean:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf code_clinic.spec
	@rm -rf .coverage

run:
	@python code_clinic.py

setup: requirements.txt
	@pip install -r requirements.txt

test:
	@python -m unittest discover -s testing/unittests/ -p "test_*.py"

coverage:
	@coverage run -m unittest discover -s testing/unittests/ -p "test_*.py"
	@coverage report

update-dependencies:
	@pipenv update
	@pipenv requirements > requirements.txt
