#!/bin/bash

echo "Total number of commits : "
git rev-list --count HEAD

echo
echo "Number of commits per author : "
git log --format="%an" | sort | uniq -c | sort -rn

echo
echo "File that has been changed in most commits : "
git log --diff-filter=M --name-only --format="" | sort | uniq -c | sort -rn | head -1

echo
echo "3 most recently modified files : "
git diff --name-only HEAD~3 HEAD
