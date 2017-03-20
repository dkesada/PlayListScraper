#! /usr/bin/python
# -*- coding: utf-8 -*-
#author: David Quesada López

import urllib2
from bs4 import BeautifulSoup
from PIL import Image
from cStringIO import StringIO
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from re import split
from time import sleep

# The playlist url, constant for now
url = 'https://www.youtube.com/playlist?list=PLPV3XXS84jhAFXrEIlNJ-gMwNqUpnTL6l'

# Fist, I have to load the full playlist with the 'Load more' button. I'll use selenium for that
driver = webdriver.Firefox()
driver.get(url)
try:
	while(True):
		wait = WebDriverWait(driver, 1)
		element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'browse-items-load-more-button')))
		element.click()
		sleep(0.5) # To avoid the stale element by clicking the same button twice
except (NoSuchElementException, TimeoutException):
	pass

html = driver.page_source
driver.quit()
soup = BeautifulSoup(html,'html.parser')

# Header
header = soup.find(id='pl-header')
imgUrl = header.find('img')['src']
img = Image.open(StringIO(urllib2.urlopen(imgUrl).read())) # Playlist thumbnail
title = header.find('h1').get_text()
title = title[5:len(title)-3] # Cleaning the title
data = header.find('ul').find_all('li')
for i in range(3):
	data[i] = data[i].get_text() # Cleaning relevant playlist information

del header

# Videos div
soup = soup.find(id='pl-load-more-destination')
videos = soup.find_all('tr')
res = [] # I'll store the tuples in another list in order to avoid inserting in O(n) in videos

for v in videos:
	try:
		imgUrl = v.find('img')['data-thumb']
	except KeyError:
		imgUrl = v.find('img')['src'] # Some of the videos have data-thumb, others have src, I don't know the reason
	
	img = Image.open(StringIO(urllib2.urlopen(imgUrl).read())) # Video thumbnail
	v = filter(None,split(' *\n *',v.get_text()))[1:4] # I use the regular expresion and the filter to clean all the data I want
	print(v)
	res.append([img] + v)
