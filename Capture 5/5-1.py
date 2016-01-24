# coding: utf-8
sumx = 0
i = 0
while True:
	try:
		x = raw_input('> ')
		if x == 'done':
			break
		else:
			x = int(x)
	except:
		print 'Error, please enter numeric input'
		continue
	sumx+=x
	i+=1
	print x
print 'Done!'
print sumx, i, sumx/i