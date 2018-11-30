#!/bin/python
import codecs
import base64

def hexstring_to_base64(string):
	return base64.b64encode(codecs.decode(string, "hex"))
