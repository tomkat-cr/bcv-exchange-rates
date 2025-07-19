.PHONY: all deactivate pipfile clean update run_module run deploy_prod rename_staging
SHELL := /bin/bash

# default show this file
all:
	@cat Makefile

deactivate:
	${SHELL} ./run.sh deactivate

pipfile:
	${SHELL} ./run.sh pipfile

clean:
	${SHELL} ./run.sh clean

update:
	${SHELL} ./run.sh update

install:
	poetry install

test:
	poetry run pytest

run:
	${SHELL} ./run.sh

run_module:
	${SHELL} ./run.sh run_module

run_vercel:
	${SHELL} ./run.sh run_vercel

deploy_prod:
	${SHELL} ./run.sh deploy_prod

rename_staging:
	${SHELL} ./run.sh rename_staging

pypi-build: clean
	# Build 'dist' directory needed for the Pypi publish
	poetry lock
	rm -rf dist
	python3 -m build

pypi-publish-test: pypi-build
	# Pypi Test publish
	python3 -m twine upload --repository testpypi dist/*

pypi-publish: pypi-build
	# Production Pypi publish
	python3 -m twine upload dist/*
