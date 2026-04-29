# Finding-to-Fix Examples

## Example 1: Dependency vulnerability

- **Finding:** `pip-audit` reports a vulnerable package version.
- **Fix:** Update `requirements.txt` to a non-vulnerable version and run tests.
- **Validation:** Re-run `make depscan` and `make test`.

## Example 2: Hardcoded secret

- **Finding:** Gitleaks flags an API token in source code.
- **Fix:** Remove token from code/history and load from environment variable.
- **Validation:** Re-run `make secretscan` and confirm no findings.

## Example 3: Container CVE

- **Finding:** Trivy reports HIGH/CRITICAL vulnerability in image.
- **Fix:** Use newer/pinned base image digest or upgrade affected package.
- **Validation:** Rebuild image and run `make containerscan`.
