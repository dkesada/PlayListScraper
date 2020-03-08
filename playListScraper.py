#! /usr/bin/python
# -*- coding: utf-8 -*-
#author: David Quesada López

from urllib2 import urlopen
from bs4 import BeautifulSoup
from PIL import Image
from cStringIO import StringIO
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from re import split


# The playlist url, constant for now
url = 'https://www.youtube.com/playlist?list=PLPV3XXS84jhAFXrEIlNJ-gMwNqUpnTL6l'

# Fist, I have to load the full playlist going to the bottom of the list. I'll use selenium for that
driver = webdriver.Chrome('./PlayListScraper/driver/chromedriver.exe')
driver.get(url)
last, current = -1, 0

try:
	while last < current:
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		last = current
		current = len(soup.find_all('div', {'id':'content'}))
		driver.execute_script('window.scrollTo(0, document.getElementById("page-manager").scrollHeight);')
except TimeoutException:
	pass

driver.quit()
soup = BeautifulSoup(driver.page_source,'html.parser')

# TODO: done up to this point

# Videos div
soup = soup.find(id='pl-load-more-destination')
videos = soup.find_all('tr')
res = [] # I'll store the tuples in another list in order to avoid inserting in O(n) in videos
l = len(videos)
t = ' out of ' + str(l) + ' processed.'
i = 1
for v in videos:
	try:
		imgUrl = v.find('img')['data-thumb']
	except KeyError:
		imgUrl = v.find('img')['src'] # Some of the videos have data-thumb, others have src, I don't know the reason
	
	img = Image.open(StringIO(urlopen(imgUrl).read())) # Video thumbnail
	v = filter(None,split(' *\n *',v.get_text()))[1:4] # I use the regular expresion and the filter to clean all the data I want
	#print(v)
	res.append([img] + v)
	print '{0}\r'.format(str(i) + t),
	i += 1

del soup
del videos

print('Process complete, generating PDF file.')

pdfTable(data, res)
