# coding: utf-8
def computegrade(score):
	try:
		if not score >1 or score<0:
			if score >= 0.9:
				grade = 'A'
			elif score >= 0.7:
				grade = 'B'
			elif score >= 0.7:
				grade = 'C'
			elif score >= 0.6:
				grade = 'D'
			elif score < 0.6:
				grade = 'F'
		else:
			print 'Bad score'
		return grade
	except:
		print 'Error, please enter numeric input'

print computegrade(99)