# coding: utf-8

import time

fname = raw_input('Enter the file name: ')
fname = 'mbox-short.txt'
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
	words = line.split()
	#print 'Debug:', words
	if len(words) >= 5 and words[0] == 'From' :
		hour = words[5].split(':')[0]
		#print'Debug:', hour,
		if not hour in counts: counts[hour]=1
		elif hour in counts: counts[hour]+=1
		#print'Debug: Used', time.time() - t1, 'Second'
		#tsum += utime
#print counts
t = list()
for key,val in counts.items():
	t.append((key,val))
	#print 'Debug:', key, val
t.sort(reverse=True)
for hour, times in t: print hour, times
print 'End:', t[0][0], t[0][1]
print 'Used', time.time()-t0, 'seconds'