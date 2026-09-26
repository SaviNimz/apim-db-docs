#!/bin/bash
# usage: step.sh <product-dir> <label>
# Snapshot + diff against the previous step; the diff is saved to $VERIFY_OUT/diffs/<product>/<label>.txt.
set -e
: "${VERIFY_OUT:?set VERIFY_OUT to an absolute scratch directory}"
HERE=$(cd "$(dirname "$0")" && pwd); P=$1; L=$2; PN=$(basename "$P")
PREV=$(cat "$VERIFY_OUT/snaps/$PN/.last" 2>/dev/null || true)
[ "$PREV" = "$L" ] && { echo "label $L already used"; exit 1; }
"$HERE/snap.sh" "$P" "$L" >/dev/null
mkdir -p "$VERIFY_OUT/diffs/$PN"
if [ -n "$PREV" ]; then
  python3 "$HERE/diff.py" "$VERIFY_OUT/snaps/$PN/$PREV" "$VERIFY_OUT/snaps/$PN/$L" --rows 4 > "$VERIFY_OUT/diffs/$PN/$L.txt"
fi
echo "$L" > "$VERIFY_OUT/snaps/$PN/.last"
echo "== $L (vs ${PREV:-nothing})"; grep -E "^[A-Z]" "$VERIFY_OUT/diffs/$PN/$L.txt" 2>/dev/null || true
