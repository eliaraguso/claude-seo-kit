#!/usr/bin/env bash
# Scaffold: copy fixture/ into the empty run workspace and build the Search Console
# export zip from gsc-csv/ (German export, same layout as Search Console's "Download CSV").
# Needs --scaffold and python3 (or python) on PATH.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ ! -d "$here/fixture" ] || [ ! -d "$here/gsc-csv" ]; then
  echo "setup.sh: fixture/ or gsc-csv/ not found next to $here" >&2
  exit 1
fi
cp -R "$here/fixture/." .
py=""
for cand in python3 python; do
  if command -v "$cand" >/dev/null 2>&1 && "$cand" -c "import zipfile" >/dev/null 2>&1; then py="$cand"; break; fi
done
if [ -z "$py" ]; then echo "setup.sh: python3 not found" >&2; exit 1; fi
"$py" - "$here/gsc-csv" "gsc-export-2026-09.zip" <<'PY'
import pathlib
import sys
import zipfile

src, dest = pathlib.Path(sys.argv[1]), sys.argv[2]
with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(src.iterdir()):
        if f.is_file():
            z.write(f, arcname=f.name)
PY
