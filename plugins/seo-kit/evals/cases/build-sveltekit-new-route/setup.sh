#!/usr/bin/env bash
# Scaffold: copy this case's fixture/ into the empty run workspace (needs --scaffold).
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ ! -d "$here/fixture" ]; then
  echo "setup.sh: fixture/ not found next to $here" >&2
  exit 1
fi
cp -R "$here/fixture/." .
