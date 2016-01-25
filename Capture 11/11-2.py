# coding: utf-8

import  re

fname = 'mbox.txt'
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()


i = list()
for line in fhand:
	x = re.findall('^New Revision:.([0-9]+)', line)
	if len(x) > 0:
		#print x
		i+=x
counts=0	
sum = 0
for val in i:
	sum += float(val)
	counts +=1
print sum/counts