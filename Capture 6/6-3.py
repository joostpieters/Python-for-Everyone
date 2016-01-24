# coding: utf-8

def count(cletter, word):
	count = 0
	for letter in word:
		if letter == cletter:
			count = count + 1
	print count
count('l','Hello')