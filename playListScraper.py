#! /usr/bin/python
#-*. coding: utf-8 -*-
#author: David Quesada López

import urllib2
from bs4 import BeautifulSoup
from bs4 import 
# The playlist url, constant for now
url = "https://www.youtube.com/playlist?list=PLPV3XXS84jhAFXrEIlNJ-gMwNqUpnTL6l"
html = urllib2.urlopen(url)
