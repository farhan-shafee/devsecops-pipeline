# DevSecOps Pipeline Portfolio Lab

A hands-on **portfolio lab** that demonstrates how to build and validate a practical DevSecOps pipeline in GitHub Actions.

> This repository is intentionally scoped as a learning and demonstration lab. It is **not** presented as a production enterprise security platform.

## Purpose

This lab shows how to shift security checks left in CI/CD by combining:

- **SAST** (Semgrep)
- **Dependency scanning** (pip-audit)
- **Secret scanning** (Gitleaks)
- **Container scanning** (Trivy)
- **Basic test + quality validation** (pytest + syntax checks)

## Repository layout

- `src/` – demo application code
- `tests/` – unit tests
- `docker/` – container build assets
- `.github/workflows/` – CI and security pipeline examples
- `docs/` – methodology and architecture notes
- `reports/` – sample scanner outputs and remediation examples
- `scripts/` – local validation helpers

## Workflow overview

1. Developer opens a pull request.
2. CI runs tests and validation checks.
3. Security jobs run SAST, dependency, secret, and container scans.
4. Findings are uploaded as artifacts and/or shown in logs.
5. Build fails if high-signal issues are detected.
6. Developer applies fixes using documented remediation guidance.

See `docs/devsecops-methodology.md` for details.

## Architecture (lab)

```text
Developer Commit/PR
        |
        v
 GitHub Actions CI
   |- test job (pytest)
   |- lint/syntax job
   |- sast job (Semgrep)
   |- dep-scan job (pip-audit)
   |- secrets job (Gitleaks)
   `- container-scan job (Trivy)
        |
        v
   Reports + Artifacts
        |
        v
  Remediation in code/requirements
```

## Quick start

### Prerequisites

- Python 3.11+
- Docker (optional, for local container scan/build)
- Make

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run locally

```bash
make test
make security
```

## Sample outputs

Sample report files are included for portfolio review:

- `reports/sample-semgrep.json`
- `reports/sample-pip-audit.json`
- `reports/sample-gitleaks.json`
- `reports/sample-trivy.txt`
- `reports/remediation/finding-to-fix.md`

These samples are illustrative and generated from this lab context, not from a production environment.

## Skills demonstrated

- Designing CI security gates for pull requests
- Using security scanners with actionable output
- Structuring remediation workflows
- Writing security-focused documentation
- Building a containerized Python service with baseline hardening steps

## Limitations

- Single-repo lab scope; no multi-environment deployment.
- No enterprise SIEM/SOAR integrations.
- No runtime EDR or cloud CSPM integration.
- Scanner policies are intentionally simple for educational clarity.

## License

MIT – see `LICENSE`.
