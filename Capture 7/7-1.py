# coding: utf-8

fname = raw_input('Enter the file name: ')
fout = open('output.txt', 'w')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

for line in fhand:
	fout.writelines(line.rstrip().upper())
fout.close()