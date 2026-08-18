#!/usr/bin/env bash
set -euo pipefail

# One-shot Project Constellation cleanup wrapper. It intentionally leaves this
# file untouched in the cleanup commit; the connector restores the normal
# publisher immediately after the cleaned content is pushed.
if [[ "${1:-}" == "Herbertofury/ProjectDump" && -d .git ]]; then
  git config user.name "Project Constellation Cleanup"
  git config user.email "actions@users.noreply.github.com"

  python3 - <<'PY'
import json
import re
from pathlib import Path

root = Path('.')
self_path = Path('tools/github-wiki/wiki-sync.sh')
target = 'Sports Group Hub'
patterns = [
    r'[ \t]*(?:,|;)?[ \t]*(?:and|with)?[ \t]*Sports Group Hub[ \t]+remains[ \t]+removed[ \t]+and[ \t]+must[ \t]+never[ \t]+be[ \t]+re-added\.?',
    r'[ \t]*(?:,|;)?[ \t]*(?:and|with)?[ \t]*Sports Group Hub[ \t]+remains[ \t]+(?:removed|excluded|absent)\.?',
    r'[ \t]*(?:,|;)?[ \t]*(?:and|with)?[ \t]*Sports Group Hub[ \t]+(?:is[ \t]+)?(?:removed|excluded|absent)\.?',
    r'[ \t]*(?:,|;)?[ \t]*(?:and|with)?[ \t]*Sports Group Hub[ \t]+(?:absence|exclusion)\b',
    r'[ \t]*(?:,|;)?[ \t]*never[ \t]+re-add[ \t]+Sports Group Hub(?:[ \t]+unless[ \t]+[^.;\n]+)?[.;]?',
    r'[ \t]*(?:,|;)?[ \t]*and[ \t]+never[ \t]+re-add[ \t]+Sports Group Hub\.?',
    r'[ \t]*(?:,|;)?[ \t]*Sports Group Hub[ \t]*:[ \t]*absent\b',
    r'[ \t]*(?:,|;)?[ \t]*Sports Group Hub[ \t]+absent[ \t]*:[ \t]*true\b',
]

def clean_string(value):
    s = value
    for pattern in patterns:
        s = re.sub(pattern, '', s, flags=re.I)
    s = re.sub(r'\bSports Group Hub\b', '', s, flags=re.I)
    s = re.sub(r'\bsportsGroupHub[A-Za-z0-9_]*\b', '', s)
    s = s.replace('removedProjectAbsent', '')
    s = re.sub(r'\b(?:forbidden|excluded|removed)-project absence\b', '', s, flags=re.I)
    s = re.sub(r'[ \t]+,', ',', s)
    s = re.sub(r',[ \t]*,+', ',', s)
    s = re.sub(r';[ \t]*;', ';', s)
    s = re.sub(r'[ \t]+\.', '.', s)
    s = re.sub(r'[ \t]+;', ';', s)
    s = re.sub(r'[ \t]{2,}', ' ', s)
    s = re.sub(r'(?m)[ \t]+$', '', s)
    s = re.sub(r'(?m)^\s*[-*]\s*$\n?', '', s)
    s = re.sub(r'(?m)^\s*[,;.]\s*$\n?', '', s)
    return s.strip() if '\n' not in value else s

def clean_obj(obj):
    if isinstance(obj, dict):
        return {k: clean_obj(v) for k, v in obj.items() if k != 'removedProjectAbsent' and not k.lower().startswith('sportsgrouphub')}
    if isinstance(obj, list):
        return [clean_obj(item) for item in obj if not (isinstance(item, dict) and str(item.get('name', '')).strip().lower() == target.lower())]
    if isinstance(obj, str):
        return clean_string(obj)
    return obj

for path in sorted(root.rglob('*')):
    if not path.is_file() or '.git' in path.parts or path == self_path or path.as_posix().startswith('.github/workflows/'):
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
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r'(?m)[ \t]+$', '', text)
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

forbidden = re.compile(r'Sports Group Hub|sportsGroupHub[A-Za-z0-9_]*|removedProjectAbsent|(?:forbidden|excluded|removed)-project absence', re.I)
left = []
for path in root.rglob('*'):
    if not path.is_file() or '.git' in path.parts or path == self_path or path.as_posix().startswith('.github/workflows/'):
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        continue
    if forbidden.search(text):
        left.append(str(path))
if left:
    raise SystemExit('references remain:\n' + '\n'.join(sorted(left)))
print('Current UTF-8 tree outside workflows and the temporary wrapper contains zero retired-project references')
PY

  git add -A
  if ! git diff --cached --quiet; then
    git diff --cached --check
    git commit -m "chore: remove retired project references"
    git pull --rebase origin main
    git push origin HEAD:main
  fi
  exit 0
fi

echo "This temporary wrapper is only valid for Herbertofury/ProjectDump." >&2
exit 71
