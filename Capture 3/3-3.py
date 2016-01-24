# coding: utf-8

try:
	score = float(raw_input('Enter your Score: '))
	if not score >1 or score<0:
		if score >= 0.9:
			print 'A'
		elif score >= 0.7:
			print 'B'
		elif score >= 0.7:
			print 'C'
		elif score >= 0.6:
			print 'D'
		elif score < 0.6:
			print 'F'
	else:
		print 'Bad score'
except:
	print 'Error, please enter numeric input'