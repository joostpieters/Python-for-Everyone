# coding: utf-8

fhand = open('mbox.txt')
counts = dict()
for line in fhand:
	words = line.split()
	#print 'Debug:', words
	if len(words) >=3 and words[0] == 'From' :
		word=words[1]
		counts[word] = counts.get(word,0) + 1
print counts