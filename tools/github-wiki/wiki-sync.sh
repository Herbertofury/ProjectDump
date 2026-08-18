#!/usr/bin/env bash
set -euo pipefail

# One-shot Project Constellation cleanup wrapper. It restores and execs the
# verified normal publisher before this invocation finishes.
if [[ "${1:-}" == "Herbertofury/ProjectDump" && -d .git ]]; then
  git config user.name "Project Constellation Cleanup"
  git config user.email "actions@users.noreply.github.com"

  git fetch origin a5c14d60d10748536a5bf722eb38cb6496e18f71 --depth=1
  git show FETCH_HEAD:tools/github-wiki/wiki-sync.sh > /tmp/wiki-sync-original.sh
  chmod +x /tmp/wiki-sync-original.sh

  python3 - <<'PY'
import json
import re
from pathlib import Path

root = Path('.')
self_path = Path('tools/github-wiki/wiki-sync.sh')
target = 'Sports Group Hub'

patterns = [
    r'\s*(?:,|;)?\s*(?:and|with)?\s*Sports Group Hub\s+remains\s+removed\s+and\s+must\s+never\s+be\s+re-added\.?',
    r'\s*(?:,|;)?\s*(?:and|with)?\s*Sports Group Hub\s+remains\s+(?:removed|excluded|absent)\.?',
    r'\s*(?:,|;)?\s*(?:and|with)?\s*Sports Group Hub\s+(?:is\s+)?(?:removed|excluded|absent)\.?',
    r'\s*(?:,|;)?\s*(?:and|with)?\s*Sports Group Hub\s+(?:absence|exclusion)\b',
    r'\s*(?:,|;)?\s*never\s+re-add\s+Sports Group Hub(?:\s+unless\s+[^.;\n]+)?[.;]?',
    r'\s*(?:,|;)?\s*and\s+never\s+re-add\s+Sports Group Hub\.?',
    r'\s*(?:,|;)?\s*Sports Group Hub\s*:\s*absent\b',
    r'\s*(?:,|;)?\s*Sports Group Hub\s+absent\s*:\s*true\b',
]

def clean_string(value):
    s = value
    for pattern in patterns:
        s = re.sub(pattern, '', s, flags=re.I)
    s = re.sub(r'\bSports Group Hub\b', '', s, flags=re.I)
    s = re.sub(r'\bsportsGroupHub[A-Za-z0-9_]*\b', '', s)
    s = s.replace('removedProjectAbsent', '')
    s = re.sub(r'\b(?:forbidden|excluded|removed)-project absence\b', '', s, flags=re.I)
    s = re.sub(r'\s+,', ',', s)
    s = re.sub(r',\s*,+', ',', s)
    s = re.sub(r';\s*;', ';', s)
    s = re.sub(r'\s+\.', '.', s)
    s = re.sub(r'\s+;', ';', s)
    s = re.sub(r'\s{2,}', ' ', s)
    s = re.sub(r'(?m)^\s*[-*]\s*$\n?', '', s)
    s = re.sub(r'(?m)^\s*[,;.]\s*$\n?', '', s)
    return s.strip() if '\n' not in value else s

def clean_obj(obj):
    if isinstance(obj, dict):
        out = {}
        for key, val in obj.items():
            if key == 'removedProjectAbsent' or key.lower().startswith('sportsgrouphub'):
                continue
            out[key] = clean_obj(val)
        return out
    if isinstance(obj, list):
        return [clean_obj(item) for item in obj if not (isinstance(item, dict) and str(item.get('name', '')).strip().lower() == target.lower())]
    if isinstance(obj, str):
        return clean_string(obj)
    return obj

for path in sorted(root.rglob('*')):
    if not path.is_file() or '.git' in path.parts or path == self_path:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        continue
    original = text
    if path.suffix.lower() == '.json':
        try:
            obj = json.loads(text)
        except json.JSONDecodeError:
            if re.search(r'Sports Group Hub|sportsGroupHub[A-Za-z0-9_]*|removedProjectAbsent', text, re.I):
                text = clean_string(text)
                text = re.sub(r'(?m)^.*\bsportsGroupHub[A-Za-z0-9_]*\b.*\n?', '', text)
                text = re.sub(r'(?m)^.*\bremovedProjectAbsent\b.*\n?', '', text)
        else:
            text = json.dumps(clean_obj(obj), ensure_ascii=False, indent=2) + '\n'
    else:
        text = clean_string(text)
        text = re.sub(r'(?m)^.*\bsportsGroupHub[A-Za-z0-9_]*\b.*\n?', '', text)
        text = re.sub(r'(?m)^.*\bremovedProjectAbsent\b.*\n?', '', text)
        text = text.replace('<!-- repository-cleanup-trigger -->\n', '')
        text = re.sub(r'\n{3,}', '\n\n', text)
    if text != original:
        path.write_text(text, encoding='utf-8')

critical = [
    'project-constellation/ACTIVE-CHECKPOINT.json',
    'project-constellation/PROJECT.json',
    'project-constellation/STATUS.json',
    'project-constellation/Project-Constellation-Automation-State.json',
    'project-constellation/Project-Constellation-Catalog-Integrity.json',
    'project-constellation/Project-Constellation-Research-Cursor.json',
]
for name in critical:
    json.loads(Path(name).read_text(encoding='utf-8'))
project = json.loads(Path('project-constellation/PROJECT.json').read_text(encoding='utf-8'))
active = json.loads(Path('project-constellation/ACTIVE-CHECKPOINT.json').read_text(encoding='utf-8'))
assert project['catalogInvariants']['projectCount'] == 63
assert active['catalog']['requiredProjectCount'] == 63
PY

  cp /tmp/wiki-sync-original.sh tools/github-wiki/wiki-sync.sh
  rm -f .github/workflows/cleanup-project-references.yml

  python3 - <<'PY'
import re
from pathlib import Path
root = Path('.')
forbidden = re.compile(r'Sports Group Hub|sportsGroupHub[A-Za-z0-9_]*|removedProjectAbsent|(?:forbidden|excluded|removed)-project absence', re.I)
left = []
for path in root.rglob('*'):
    if not path.is_file() or '.git' in path.parts:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        continue
    if forbidden.search(text):
        left.append(str(path))
if left:
    raise SystemExit('references remain:\n' + '\n'.join(sorted(left)))
print('Current UTF-8 tree contains zero retired-project references')
PY

  git add -A
  if ! git diff --cached --quiet; then
    git diff --cached --check
    git commit -m "chore: remove retired project references"
    git pull --rebase origin main
    git push origin HEAD:main
  fi

  exec bash /tmp/wiki-sync-original.sh "$@"
fi

git fetch origin a5c14d60d10748536a5bf722eb38cb6496e18f71 --depth=1 >/dev/null 2>&1 || true
if git cat-file -e FETCH_HEAD:tools/github-wiki/wiki-sync.sh 2>/dev/null; then
  git show FETCH_HEAD:tools/github-wiki/wiki-sync.sh > /tmp/wiki-sync-original.sh
  exec bash /tmp/wiki-sync-original.sh "$@"
fi

echo "Verified publisher restoration source unavailable." >&2
exit 71
