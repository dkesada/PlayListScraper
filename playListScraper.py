#! /usr/bin/python
#-*. coding: utf-8 -*-
#author: David Quesada López

import urllib2
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from PIL import Image
from cStringIO import StringIO

# The playlist url, constant for now
url = "https://www.youtube.com/playlist?list=PLPV3XXS84jhAFXrEIlNJ-gMwNqUpnTL6l"
html = urllib2.urlopen(url)

soup = BeautifulSoup(html,"html.parser")


# Header
header = soup.find(id="pl-header")
imgUrl = header.find('img')['src']
img = Image.open(StringIO(urllib2.urlopen(imgUrl).read())) # Playlist thumbnail
title = header.find('h1').get_text()
title = title[5:len(title)-3] # Cleaning the title
data = header.find('ul').find_all('li')
for i in range(3):
	data[i] = data[i].get_text() # Cleaning relevant playlist information

del header

# Videos div
soup = soup.find(id="pl-video-list")
