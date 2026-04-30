.PHONY: install validate test sast depscan secretscan containerscan security

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-security.txt

validate:
	python -m py_compile src/example_app.py tests/test_example_app.py
	pytest -q -p no:cacheprovider

test:
	pytest -q -p no:cacheprovider

sast:
	semgrep scan --config auto --error src

depscan:
	pip-audit -r requirements.txt --strict

secretscan:
	docker run --rm -v "$$(pwd):/path" zricethezav/gitleaks:v8.30.1 detect --source=/path

containerscan:
	docker build -t devsecops-lab:local -f docker/Dockerfile .
	docker run --rm aquasec/trivy:v0.70.0 image --severity HIGH,CRITICAL --vuln-type os,library --ignore-unfixed --exit-code 1 devsecops-lab:local

security: sast depscan secretscan containerscan
