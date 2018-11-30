#!/bin/python

def isPrintable(hexstring):
	result = True
	for i in xrange(len(hexstring)/2):
		idx = i*2
		chx = hexstring[idx:idx+2]
		if int(chx, 16) < 32 or int(chx, 16) > 127:
				# control character exceotions: NUL, LF, CR
				if int(chx, 16) in [0, 10, 13]:
					pass
				else:
					result = False
					break
	return result
