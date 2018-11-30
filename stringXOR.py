#!/bin/python

def stringXOR(string1, string2):
	string1 = string1.encode("hex")
	string2 = string2.encode("hex")
	#print string1, string2
	return format(int(string1, 16)^int(string2, 16), 'x').zfill(len(string1))

#s1="Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
#s2="ICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEIC"
#print stringXOR(s1, s2)
#0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20690a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

