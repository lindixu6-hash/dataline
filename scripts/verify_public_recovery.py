#!/usr/bin/env python3

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / ".github/workflows/test.yml").read_text()

assert (ROOT / ".nvmrc").read_text().strip() == "20.19.5"
assert (ROOT / ".python-version").read_text().strip() == "3.11"
assert re.search(r"^permissions:\n  contents: read$", WORKFLOW, re.MULTILINE)
assert "runs-on: ubuntu-22.04" in WORKFLOW
assert 'version: "0.8.14"' in WORKFLOW
assert "uv sync --frozen" in WORKFLOW
assert "uv run pytest tests" in WORKFLOW
assert "uv run python -m compileall -q dataline" in WORKFLOW
assert "npm ci" in WORKFLOW
assert "npm run build" in WORKFLOW

for forbidden in (
    "${{ secrets.",
    "docker/login-action",
    "docker/build-push-action",
    "npm publish",
    "uv publish",
    "pyinstaller",
):
    assert forbidden not in WORKFLOW, f"Recovery CI contains forbidden operation: {forbidden}"

actions = re.findall(r"^\s*uses:\s*(\S+)", WORKFLOW, re.MULTILINE)
assert actions, "Recovery CI must use pinned actions"
for action in actions:
    assert re.fullmatch(
        r"[^@\s]+@[0-9a-f]{40}", action
    ), f"Action is not pinned to a full commit SHA: {action}"

print("Public recovery contract verified")
