# coding: utf-8

fhand = open('mbox.txt')
count = 0
for line in fhand:
	words = line.split()
	#print 'Debug:', words
	if len(words) != 0 and len(words) != 1 and words[0] == 'From' : print words[1]