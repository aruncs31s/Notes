#!/bin/zsh
git status
read a 
git add -A 
git commit -m "update from mac"
git push origin macbook
