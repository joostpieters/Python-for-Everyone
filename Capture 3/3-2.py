# coding: utf-8

try:
	hours = int(raw_input('Enter Hours: '))
	rate = int(raw_input('Enter Rate: '))
	if hours > 40:
		print 'Pay: %d' % (40*rate+(hours-40)*rate*1.5)
	else:
		print 'Pay: %d' % (hours*rate)
except:
	print 'Error, please enter numeric input'