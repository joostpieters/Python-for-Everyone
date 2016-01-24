# coding: utf-8
def computepay(hours, rate):
	try:
		if hours > 40:
			print 'Pay: %d' % (40*rate+(hours-40)*rate*1.5)
		else:
			print 'Pay: %d' % (hours*rate)
	except:
		print 'Error, please enter numeric input'