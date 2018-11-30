#!/bin/python

def stringHammingDistance(string1, string2):
	# The Hamming/Edit distance is just the number of differing bits.
	string1 = string1.encode("hex")
	string2 = string2.encode("hex")
	#print string1, string2
	return bin(int(string1, 16)^int(string2, 16)).count('1')

#s1 = 'this is a test'
#s2 = 'wokka wokka!!!'

#print stringHammingDistance(s1,s2)
#37

