#!/usr/bin/env bash
set -e

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

git add -A
git commit -m "Backup: ${TIMESTAMP}" || echo "Nothing to commit"
git pull origin main || { echo "Pull failed - please resolve conflicts manually"; exit 1; }
git push origin main
