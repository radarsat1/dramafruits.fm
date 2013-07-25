#!/bin/sh

python get.py >out.html
git checkout gh-pages
mv out.html index.html
git add index.html
git commit -m "$(date)"
git checkout master
