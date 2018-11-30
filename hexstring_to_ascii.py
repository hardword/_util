#!/bin/python
import codecs

def hexstring_to_ascii(string):
	return codecs.decode(string, "hex")

#def hexstring_to_ascii(string):
#	result = ''
#	for i in xrange(len(string)/2):
#		result += chr(int(string[i*2:i*2+2],16))
#	return result

#def hexstring_to_ascii(string):
#	return bytearray.fromhex(string)

