# coding: utf-8
import re
import socket
url=raw_input('Enter URL>')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
furl = url.split('/')
try:
	#print furl[2]
	mysock.connect((furl[2],80))
	#print 'GET '+url+' HTTP/1.0\n\n'
	mysock.send('GET '+url+' HTTP/1.0\n\n')
except:
	print furl
	if len(url) > 1 and furl[0] != 'http:':
		print 'Plese add http:// before URL'
	else:
		print 'Plese check the URL and enter true URL'
	exit()
html=''
while True:
	data = mysock.recv(2048)
	if ( len(data) < 1 ) :
		break
	html+=data
mysock.close()

print html[html.find('\r\n\r\n')+4:]

	
	