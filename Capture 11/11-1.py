# coding: utf-8

import  re

regular = raw_input('Enter a regular expression: ')
fname = 'mbox.txt'
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

counts = 0
for line in fhand:
	if re.search(regular, line):
		counts+=1

print counts