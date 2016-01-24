# coding: utf-8

data = 'X-DSPAM-Confidence: 0.8475'
x = data.find(':')
print float(data[x+2:])