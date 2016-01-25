# coding: utf-8

import string
import time
string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~1234567890'

fname = raw_input('Enter the file name: ')
fname = 'mbox.txt'
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
	
t0 = time.time()
counts = dict()
tsum = 0.0
for line in fhand:
	t1 = time.time()
	line = line.translate(None,string.punctuation).lower()
	words = line.split()
	#print 'Debug:', words
	for word in words:
		for char in word:
			if not char in counts: counts[char]=1
			elif char in counts: counts[char]+=1
		#print'Debug: Used', time.time() - t1, 'Second'
		#tsum += utime
#print counts
t = list()
for key,val in counts.items():
	t.append((val,key))
	#print 'Debug:', key, val
t.sort(reverse=True)
for key, val in t: print val, key
print 'End:', t[0][1], t[0][0]
print 'Used', time.time()-t0, 'seconds'