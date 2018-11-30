#!/bin/python

def hexstringXOR(string1, string2):
	return format(int(string1, 16)^int(string2, 16), 'x')

s1="1c0111001f010100061a024b53535009181c"
s2="686974207468652062756c6c277320657965"

print hexstringXOR(s1, s2)
#746865206b696420646f6e277420706c6179