# DevSecOps Methodology (Portfolio Lab)

## Goals

- Catch common security issues early in pull requests.
- Produce actionable findings with clear remediation paths.
- Keep controls understandable and reproducible.

## Pipeline stages

1. **Code quality & tests**
   - Basic syntax validation and unit tests.
2. **SAST**
   - Semgrep scans application source for insecure patterns.
3. **Dependency scanning**
   - `pip-audit` flags known vulnerable dependencies.
4. **Secret detection**
   - Gitleaks detects exposed credentials and tokens.
5. **Container image scanning**
   - Trivy checks base image and package vulnerabilities.

## Security gate strategy

- Fail fast on high-confidence scanner failures.
- Capture machine-readable reports for triage.
- Apply remediation and re-run pipeline before merge.

## Triage approach

- Prioritize by exploitability and asset exposure.
- Distinguish true positive vs. false positive.
- Record compensating controls where risk is accepted.

## Portfolio framing

This repository demonstrates security engineering workflow mechanics and communication quality. It intentionally avoids claims about enterprise scale or production SLA outcomes.
