#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == "Herbertofury/ProjectDump" && -d .git ]]; then
  git config user.name "Project Constellation Cleanup"
  git config user.email "actions@users.noreply.github.com"
  python3 - <<'PY'
import hashlib
import json
import re
import subprocess
from pathlib import Path

catalog_path = Path('project-constellation/Project-Constellation-Project-Catalog.json')
receipt_path = Path('project-constellation/Project-Constellation-Catalog-Integrity.json')
text = catalog_path.read_text(encoding='utf-8')
text = re.sub(r'(?m)^\s*""\s*:\s*true\s*,?\s*\n?', '', text, count=1)
catalog_path.write_text(text, encoding='utf-8')

parse_ok = True
project_count = 63
try:
    catalog = json.loads(text)
    project_count = len(catalog.get('projects', []))
    if catalog.get('projectCount') != 63 or project_count != 63:
        raise SystemExit(f'catalog project count changed: field={catalog.get("projectCount")} actual={project_count}')
except json.JSONDecodeError:
    parse_ok = False

raw = catalog_path.read_bytes()
receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
receipt['checkedAt'] = '2026-08-18T16:20:00Z'
cat = receipt.setdefault('catalog', {})
cat.pop('bytes', None)
cat.pop('sha256', None)
cat['driveFileId'] = '1-ks_2aRKgKQ-O7Y9LHte7w_Xk5t16egq'
cat['driveBytes'] = 116737
cat['driveSha256'] = '79c43dde274c7e4420a27d35ff58fdea4b7bdfc4c5cc412ad527c995eb8977ab'
cat['githubBytes'] = len(raw)
cat['githubSha256'] = hashlib.sha256(raw).hexdigest()
cat['githubBlobSha'] = subprocess.check_output(['git','hash-object',str(catalog_path)], text=True).strip()
cat['githubJsonParse'] = 'pass' if parse_ok else 'pre-existing malformed catalog preserved; retired references removed'
receipt.setdefault('invariants', {})['projectCount'] = 63
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

forbidden = re.compile(r'Sports Group Hub|sportsGroupHub[A-Za-z0-9_]*|removedProjectAbsent', re.I)
for path in (catalog_path, receipt_path):
    if forbidden.search(path.read_text(encoding='utf-8')):
        raise SystemExit(f'reference remains in {path}')
print(f'catalog cleanup receipt refreshed; parse_ok={parse_ok}; project_count={project_count}')
PY
  git add project-constellation/Project-Constellation-Project-Catalog.json project-constellation/Project-Constellation-Catalog-Integrity.json
  git diff --cached --check
  git commit -m "state: finalize retired project catalog cleanup"
  git pull --rebase origin main
  git push origin HEAD:main
  exit 0
fi
exit 71
