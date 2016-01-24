# coding: utf-8
x = None
maxx = None
minx = None
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
	if maxx is None or minx is None:
		maxx=x
		minx=x
	maxx = max(maxx, x)
	minx = min(minx, x)
print 'Done!'
print maxx, minx