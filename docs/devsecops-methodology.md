# DevSecOps Methodology

This lab uses a shift-left approach:

1. Keep application code simple and testable.
2. Run fast CI checks on every change.
3. Run security checks in dedicated jobs for clear ownership.
4. Fail quickly on actionable findings.
5. Document remediation decisions.

## Principles

- Minimal dependencies reduce attack surface.
- Security gates are explicit and reviewable.
- Scan outputs are preserved as examples in `reports/`.
- Findings should result in code or dependency changes, not hidden suppressions.
