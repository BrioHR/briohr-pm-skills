#!/usr/bin/env bash
#
# build-zips.sh — regenerate the ready-to-upload skill zips in dist/.
#
# Each skill folder under skills/ becomes a zip with SKILL.md at its root,
# which is the structure Claude's Skills uploader expects. Each skill folder
# also carries its own vendored knowledge-base/, so the zip is self-contained
# and the skill can ground its output offline.
#
# Usage:
#   ./scripts/build-zips.sh
#
set -euo pipefail

# Move to the repo root (parent of this script's directory), so the script
# works no matter where it's called from.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

SKILLS_DIR="skills"
DIST_DIR="dist"

if ! command -v zip >/dev/null 2>&1; then
  echo "error: 'zip' is not installed." >&2
  exit 1
fi

if [ ! -d "$SKILLS_DIR" ]; then
  echo "error: no '$SKILLS_DIR/' directory found." >&2
  exit 1
fi

mkdir -p "$DIST_DIR"

count=0
for skill_path in "$SKILLS_DIR"/*/; do
  [ -d "$skill_path" ] || continue
  skill_name="$(basename "$skill_path")"

  if [ ! -f "$skill_path/SKILL.md" ]; then
    echo "skip: $skill_name has no SKILL.md"
    continue
  fi

  zip_file="$REPO_ROOT/$DIST_DIR/$skill_name.zip"
  rm -f "$zip_file"

  # Zip from inside the skill folder so SKILL.md (and the skill's bundled
  # knowledge-base/) land at the zip root. Exclude dotfiles (e.g. .DS_Store).
  ( cd "$skill_path" && zip -q -r "$zip_file" . -x '.*' -x '*/.*' )

  echo "built: $DIST_DIR/$skill_name.zip"
  count=$((count + 1))
done

echo ""
echo "Done. $count skill zip(s) in $DIST_DIR/."
echo "Next: upload each zip in Claude (Settings -> Capabilities -> Skills),"
echo "or attach them to a GitHub Release:  gh release create vX.Y.Z dist/*.zip"
