#!/bin/bash
cd "$CLAUDE_PROJECT_DIR" || exit 0
echo "Second brain state."
[ -f wiki/hot.md ] && { echo "--- wiki/hot.md ---"; cat wiki/hot.md; }
echo "--- pending ingest ---"
python3 brain.py status 2>&1
exit 0
