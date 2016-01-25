# coding: utf-8

import time

fname = raw_input('Enter the file name: ')
#fname = 'mbox.txt'
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
	
t0 = time.time()
counts = dict()
for line in fhand:
	words = line.split()
	#print 'Debug:', words
	if len(words) >=3 and words[0] == 'From' :
		email = words[1]
		if not email in counts: counts[email]=1
		elif email in counts: counts[email]+=1
#print counts
t = list()
for key,val in counts.items():
	t.append((val,key))
	#print 'Debug:', key, val
t.sort(reverse=True)

print t[0][1], t[0][0], 'Used', time.time()-t0, 'seconds'