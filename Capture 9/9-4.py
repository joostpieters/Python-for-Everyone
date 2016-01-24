# coding: utf-8

fname = raw_input('Enter the file name: ')
#fname = 'mbox.txt'
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

counts = dict()
for line in fhand:
	words = line.split()
	#print 'Debug:', words
	if len(words) >=3 and words[0] == 'From' :
		word=words[1]
		counts[word] = counts.get(word,0) + 1
count = None
for i in counts:
	if counts[i] > count :
		count = counts[i]
		email = i

print email, count
		