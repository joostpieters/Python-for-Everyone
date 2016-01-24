# coding: utf-8

numbers = []
while True:
	try:
		x = raw_input('Enter a Number: ')
		if x == 'done':
			print 'Done!'
			break
		else:
			numbers.append(int(x))
	except:
		print 'Error, please enter numeric input'
		continue
	
if len(numbers) != 0:
	print 'Maximum:', max(numbers), 'Minimun:', min(numbers)
else:
	print 'Have No Number'