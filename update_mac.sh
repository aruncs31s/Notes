#!/bin/bash

# Check if which one contains the gmail aruncs31ss@gmail.com

for file in ~/.ssh/*; do
    if grep -q "aruncs31ss"
    then
        file=$(basename "$file")
        echo "Found aruncs31ss in $file"
    fi
done

GIT_SSH_COMMAND="ssh -i $file " git pull origin main

# GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa.bak" git pull origin main
