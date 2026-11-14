#!/bin/bash
f=$(jq -r '.tool_input.file_path // empty')
case "$f" in */wiki/*) cd "$CLAUDE_PROJECT_DIR" && python3 brain.py lint >&2 || exit 2;; esac
exit 0
