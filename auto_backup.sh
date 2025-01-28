#!/bin/env bash

git add -A
git commit -m "update $(date)"

git pull origin main

git push orign main
# echo "update $(date)"
