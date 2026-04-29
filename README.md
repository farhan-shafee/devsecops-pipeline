# DevSecOps Portfolio Lab

This repository is a **learning and portfolio lab** that demonstrates a clean DevSecOps CI/CD pipeline on a small Python example project.

> It is intentionally scoped for demonstration and education. It is **not** a production system.

## What this pipeline demonstrates

- CI validation (format/sanity checks, compile checks, tests)
- SAST with Bandit
- Dependency vulnerability scanning with pip-audit
- Secret scanning with Gitleaks
- Container vulnerability scanning with Trivy

## Repository layout

- `src/example_app.py` – minimal Python standard-library app logic
- `tests/test_example_app.py` – pytest unit tests
- `scripts/validate.sh` – local validation helper
- `docker/Dockerfile` – minimal non-root container image
- `.github/workflows/ci.yml` – CI checks
- `.github/workflows/security.yml` – security scanning jobs
- `reports/` – static sample scan outputs for documentation purposes only
- `docs/` – methodology, pipeline overview, and remediation notes

## Local usage

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-security.txt
make test
make validate
make sast
make audit
make docker-build
```

## GitHub Actions checks

- **CI workflow** runs:
  - dependency install
  - unit tests (`pytest`)
  - Python compile check (`py_compile`)
  - shell validation script (`scripts/validate.sh`)
- **Security workflow** runs separate jobs:
  - `sast-bandit`
  - `dependency-scan`
  - `secret-scan`
  - `container-scan`

## Out of scope (intentional)

- No production deployment
- No enterprise compliance claims
- No SLA/SLO guarantees
- No runtime secret-management implementation

See `docs/` for scan interpretation and remediation workflow guidance.
