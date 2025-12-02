#!/usr/bin/env bash
set -e

echo "Updating notes from remote..."
git pull origin main
git submodule update --init --recursive
echo "Update complete!"
