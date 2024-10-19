.PHONY: testing lintting documentation

.DEFAULT_GOAL := invalid-command

invalid-command:
	@echo "[image-transformer]: please specify a target. Nothing to do."

testing:
	poetry run tox -e test

linting:
	poetry run tox -e lint

documentation:
	poetry run sphinx-apidoc -o docs/ image_transformer/
	poetry run sphinx-build -b html docs docs/_build