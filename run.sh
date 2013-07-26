#!/bin/sh

BRANCH="$(basename $(cat .git/HEAD | cut -d' ' -f2))"
mkdir tmp
python get.py >tmp/index.html
cp style.css tmp/
cp background.jpg tmp/
cp tweetbg.jpg tmp/
git checkout gh-pages
mv tmp/* .
rmdir tmp
git add index.html style.css background.jpg tweetbg.jpg
git commit -m "$(date)"
git checkout "$BRANCH"
