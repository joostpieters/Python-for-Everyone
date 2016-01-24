# coding: utf-8

fname = raw_input('Enter the file name: ')
fname = 'romeo.txt'
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
t = []
for line in fhand:
	words = line.split()
	for i in words:
		if not i in t:
			t.append(i)
t.sort()

print t