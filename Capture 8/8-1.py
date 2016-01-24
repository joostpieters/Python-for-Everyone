# coding: utf-8

letters = ['a', 'b', 'c', 'd', 'e']

def chop(t):
	del t[0]
	del t[len(t)-1]
def middle(t):
	return t[1:len(letters)-1]

print letters
print chop(letters)
print letters
print middle(letters)