import string
string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

fname = raw_input('Enter the file name: ')
counts = dict()
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
	
count = 0
for line in fhand:
	line = line.translate(None,string.punctuation)
	line = line.lower()
	words =line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1
print counts
#for key in counts:
#	print key, counts[key]