#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: wiki-sync.sh OWNER/REPO SOURCE_DIR [GITHUB_SERVER_URL]

Required environment:
  GH_TOKEN   Token with write access to the target repository.

Behavior:
  - clones OWNER/REPO.wiki.git when it already exists;
  - falls back to an empty Git repository for first-push bootstrap;
  - mirrors SOURCE_DIR exactly into the wiki Git repository;
  - commits only when content changed;
  - pushes the wiki master branch;
  - fresh-clones the published wiki and byte-compares it to SOURCE_DIR.

Creating a source file creates a wiki page, replacing it edits that page, and
removing it deletes that page on the next sync.
EOF
}

if [[ $# -lt 2 || $# -gt 3 ]]; then
  usage >&2
  exit 64
fi

repo="$1"
source_dir="$2"
server_url="${3:-${GITHUB_SERVER_URL:-https://github.com}}"
token="${GH_TOKEN:-}"

if [[ -z "$token" ]]; then
  echo "GH_TOKEN is required" >&2
  exit 65
fi
if [[ ! "$repo" =~ ^[^/[:space:]]+/[^/[:space:]]+$ ]]; then
  echo "Repository must be OWNER/REPO" >&2
  exit 64
fi
if [[ ! -d "$source_dir" ]]; then
  echo "Source directory does not exist: $source_dir" >&2
  exit 66
fi
if [[ ! -f "$source_dir/Home.md" ]]; then
  echo "Source directory must contain Home.md so the wiki has a homepage" >&2
  exit 66
fi

source_dir="$(cd "$source_dir" && pwd)"
server_url="${server_url%/}"
remote_url="$server_url/$repo.wiki.git"
work_dir="$(mktemp -d)"
wiki_dir="$work_dir/wiki"
verify_dir="$work_dir/verify"
trap 'rm -rf "$work_dir"' EXIT

auth_b64="$(printf 'x-access-token:%s' "$token" | base64 | tr -d '\r\n')"
git_auth() {
  git -c "http.extraHeader=AUTHORIZATION: basic $auth_b64" "$@"
}

existing=1
if ! git_auth clone --depth 1 "$remote_url" "$wiki_dir"; then
  existing=0
  mkdir -p "$wiki_dir"
  git -C "$wiki_dir" init -b master
  git -C "$wiki_dir" remote add origin "$remote_url"
fi

find "$wiki_dir" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -a "$source_dir"/. "$wiki_dir"/
rm -rf "$wiki_dir/.github"

git -C "$wiki_dir" config user.name 'github-actions[bot]'
git -C "$wiki_dir" config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git -C "$wiki_dir" add -A

if git -C "$wiki_dir" diff --cached --quiet; then
  echo "Wiki already matches source; nothing to publish."
else
  git -C "$wiki_dir" commit -m "Sync wiki from $repo"
  if ! git_auth -C "$wiki_dir" push --set-upstream origin HEAD:master; then
    if [[ $existing -eq 0 ]]; then
      echo "Initial wiki push failed. GitHub requires one initial page to exist before cloning/pushing the wiki Git repository." >&2
      exit 69
    fi
    exit 69
  fi
fi

git_auth clone --depth 1 "$remote_url" "$verify_dir"
rm -rf "$verify_dir/.git"

if ! diff -qr "$source_dir" "$verify_dir"; then
  echo "Remote wiki verification failed: published bytes differ from source." >&2
  exit 70
fi

published_commit="$(git_auth ls-remote "$remote_url" refs/heads/master | awk '{print $1}')"
echo "Wiki sync verified: $server_url/$repo/wiki"
echo "Wiki master commit: $published_commit"
