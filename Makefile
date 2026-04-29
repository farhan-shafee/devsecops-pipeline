.PHONY: install test validate sast audit docker-build

install:
	pip install -r requirements.txt
	pip install -r requirements-security.txt

test:
	pytest -q

validate:
	scripts/validate.sh

sast:
	bandit -q -r src/

audit:
	pip-audit -r requirements.txt

docker-build:
	docker build -t devsecops-lab:latest -f docker/Dockerfile .
