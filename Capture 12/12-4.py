# coding: utf-8

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('p')
#print tags
count = 0
for tag in tags:
	#print '\nDebug: ', tag
	count+=1
print count