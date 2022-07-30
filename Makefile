update-dependencies:
	@echo "Updating dependencies..."
	@sleep 2
	@pipenv update
	@pipenv requirements > requirements.txt
	@echo "Updated dependencies"
	@sleep 2
