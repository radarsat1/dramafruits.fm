#!/bin/sh

BRANCH="$(basename $(cat .git/HEAD | cut -d' ' -f2))"
python get.py >out.html
cp style.css __tmp.css
git checkout gh-pages
mv out.html index.html
mv __tmp.css style.css
git add index.html style.css
git commit -m "$(date)"
git checkout "$BRANCH"
