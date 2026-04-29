# Remediation Notes

Use this workflow for findings:

1. Reproduce finding locally.
2. Confirm exploitability and impact.
3. Prefer fixing root cause over suppressing rules.
4. Document reasoning in commit or PR notes.
5. Re-run relevant checks before merge.

## Typical actions

- SAST issue: update code path, input handling, or unsafe usage.
- Dependency issue: upgrade or replace package.
- Secret issue: remove secret and rotate credentials in real environments.
- Container issue: update base image or reduce image contents.
