.PHONY: install test sast depscan secretscan containerscan security

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-security.txt

test:
	pytest -q

sast:
	semgrep scan --config auto src

depscan:
	pip-audit -r requirements.txt --strict

secretscan:
	docker run --rm -v "$$(pwd):/path" zricethezav/gitleaks:latest detect --source=/path

containerscan:
	docker build -t devsecops-lab:local -f docker/Dockerfile .
	docker run --rm aquasec/trivy:latest image --severity HIGH,CRITICAL devsecops-lab:local

security: sast depscan secretscan containerscan
