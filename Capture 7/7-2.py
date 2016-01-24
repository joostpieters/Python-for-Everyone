# coding: utf-8

fname = raw_input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	if fname == 'na na boo boo':
		print "NA NA BOO BOO TO YOU - You have been punk'd!"
	print 'File cannot be opened:', fname
	exit()
	
xdspam = 0
i=0
for line in fhand:
	if line.startswith('X-DSPAM-Confidence'):
		x = line.find(':')
		xdspam += float(line[x+2:])
		i+=1
print xdspam/i