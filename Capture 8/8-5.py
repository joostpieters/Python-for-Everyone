# coding: utf-8

fhand = open('mbox.txt')
count = 0
text = []
for line in fhand:
	words = line.split()
	#print 'Debug:', words
	if len(words) != 0 and len(words) != 1 and words[0] == 'From' :
		#if not words[1] in text:
			text.append(words[1])
			count+=1
for i in text : print i
print "There were", count, "lines in the file with From as the first"