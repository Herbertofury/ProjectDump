#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == "Herbertofury/ProjectDump" && -d .git ]]; then
  git config user.name "Project Constellation Cleanup"
  git config user.email "actions@users.noreply.github.com"
  python3 - <<'PY'
import json
from pathlib import Path

handoff = Path('project-constellation/HANDOFF.md')
text = handoff.read_text(encoding='utf-8')
old = 'The v0.5.0 line contains exactly 63 tracked records and keeps It retains quick checkpoints'
new = 'The v0.5.0 line contains exactly 63 tracked records. It retains quick checkpoints'
if old not in text:
    raise SystemExit('expected handoff cleanup sentence not found')
handoff.write_text(text.replace(old, new, 1), encoding='utf-8')

state_path = Path('project-constellation/Project-Constellation-Automation-State.json')
state = json.loads(state_path.read_text(encoding='utf-8'))
state['updatedAt'] = '2026-08-18T16:28:00Z'
state['lastAutomationHash']['Project-Constellation-Project-Catalog.json'] = '79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab'
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
PY
  git add project-constellation/HANDOFF.md project-constellation/Project-Constellation-Automation-State.json
  git diff --cached --check
  git commit -m "state: finalize retired project cleanup"
  git pull --rebase origin main
  git push origin HEAD:main
  exit 0
fi
exit 71
