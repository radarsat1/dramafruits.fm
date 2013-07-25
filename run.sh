#!/bin/sh

BRANCH="$(basename $(cat .git/HEAD | cut -d' ' -f2))"
python get.py >out.html
git checkout gh-pages
mv out.html index.html
git add index.html
git commit -m "$(date)"
git checkout "$BRANCH"
