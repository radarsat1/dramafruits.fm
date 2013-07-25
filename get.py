#!/usr/bin/env python

from bs4 import BeautifulSoup as BS
import urllib2, re
from itertools import repeat

users = ['SmokedMeatFM',
         'radarsat1',
         'VanessaY']

fruitmatcher = re.compile('fruit|peach|plum', re.IGNORECASE).search

def get_user(user):
    html = open(user).read()
    #html = urllib2.urlopen('http://twitter.com/'+user).read()

    soup = BS(html)
    tweets = soup.find_all('p', class_='tweet-text')

    text = [t.text for t in tweets if fruitmatcher(t.text)]

    return zip(text, repeat(user))

def collect_all():
    all_text = []
    for u in users:
        all_text += get_user(u)
    return all_text

def generate_html(all_text):
    print '<html><head><title>DramaFruits.fm</title>'
    print '<link rel="stylesheet" type="text/css" href="style.css"/>'
    print '</head><body>'
    print '<h1>dramafruits.fm</h1>'
    print '<h2>A site dedicated to fruit-related drama occurring within the worldwide <a href="http://skweee.com">skweee</a> scene</h2>'
    for text, user in all_text:
        print '<div class="tweet"><p class=tweet-text>"'+text+'"</p>'
        print '<p class="tweet-author">&mdash;<a href="http://twitter.com/'+user+'">'+user+'</a></p></div>'
    print '</body>'

generate_html(collect_all())
