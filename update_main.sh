#!/bin/bash
set -e  # stop if any command fails

BRANCH=${1:-revision}

git switch -c "$BRANCH" || git switch "$BRANCH"
git add .
git commit -m "${2:-update}"
git pull --rebase origin "$BRANCH"
git push -u origin "$BRANCH"
git switch main
git pull origin main
git merge "$BRANCH" --no-edit
git push origin main
git branch -d "$BRANCH"
git push origin --delete "$BRANCH"

echo "✅ Merged $BRANCH into main successfully!"
