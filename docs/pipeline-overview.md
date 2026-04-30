# Pipeline Overview

## CI (`.github/workflows/ci.yml`)

- Checkout repository
- Set up Python 3.11 with pip dependency caching
- Install `requirements.txt`
- Install pinned pytest
- Run `make validate`, which performs compile checks and pytest with cache disabled

## Security (`.github/workflows/security.yml`)

### `sast-semgrep`
Runs Semgrep over `src/`, uploads SARIF, and fails the job on findings.

### `dependency-scan`
Runs pip-audit against `requirements.txt` and uploads the JSON report even when the scan fails.

### `secret-scan`
Runs Gitleaks with full history checkout and read-only pull request permissions.

### `container-scan`
Builds container and scans with Trivy.
Configured to fail on fixed actionable **HIGH** and **CRITICAL** findings.
