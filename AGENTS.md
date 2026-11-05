# AGENTS.md

Guidance for contributors and coding agents working in this repository.

## Purpose

This repository holds GitHub Agentic Workflows (gh-aw) that maintain the
repository, plus a small example greeting CLI they operate on.

## Layout

- `src/greet.py`: greeting CLI (Python 3, standard library only). Supports
  `--recipient` (default `World`).
- `tests/test_greet.py`: `unittest` tests that run the CLI as a subprocess.
- `README.md`: user-facing CLI documentation.
- `.github/workflows/*.md`: agentic workflow sources (daily documentation sync,
  weekly repository maintainer, weekly AGENTS maintenance).
- `.github/workflows/*.lock.yml`: compiled workflows, marked generated in
  `.gitattributes`.

## Commands

- Run the CLI from the repository root: `python src/greet.py [--recipient NAME]`.
- Tests use `unittest`; run them from the repository root, for example
  `python -m unittest discover -s tests`.
- Workflow `.md` files are compiled to `.lock.yml` with the gh-aw CLI
  (`gh aw compile <workflow-name> --strict --validate`, as used in merged PRs
  #1 and #3).

## Conventions

- Do not hand-edit `*.lock.yml`; edit the `.md` source and recompile so both are
  committed together.
- Keep the CLI standard-library only.
- Update `README.md` when CLI options or behavior change.
- Workflows propose draft PRs for human review; they never merge. Each workflow
  limits which files it may change, so keep changes within a workflow's
  allowed scope.
