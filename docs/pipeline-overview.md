# Pipeline Overview

## CI (`.github/workflows/ci.yml`)

- Checkout repository
- Set up Python 3.12
- Install `requirements.txt`
- Run tests with `pytest`
- Compile check: `python -m py_compile src/example_app.py`
- Run `scripts/validate.sh`

## Security (`.github/workflows/security.yml`)

### `sast-bandit`
Runs Bandit over `src/` and fails on medium/high findings.

### `dependency-scan`
Runs pip-audit against `requirements.txt`.

### `secret-scan`
Runs Gitleaks with `GITHUB_TOKEN` set from `secrets.GITHUB_TOKEN`.

### `container-scan`
Builds container and scans with Trivy.
Configured to fail only on unfixed actionable **CRITICAL** findings.
