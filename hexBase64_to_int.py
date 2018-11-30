#!/bin/python

# decode base64 string to hex int for calculation
from base64 import b64decode

def hexBase64_to_int(string):
	# b64decode(string).encode('hex') ==> can use this for hex string
	return int(b64decode(string).encode('hex'), 16)

#s1='a+iiKCqMJI5fxHsKkiZqOB8uFgqhIkaBPLzK+mREtEJvdH6M4wRH5EakoJRQHDG6CivAnZl6w79gurJnOB+YS7Qddfxl44MMuOlQ2AGU4g/NHBfmiZtgScWvFe/pl8CWFnWSWn7DeZjNm1SaXyNBOryLXkmwPcqSQBogdtSKiJMwW/+tOCOhgGd+Fu0leDNGr+AoiYjzBtbFMhRMbk5QfA=='
#s2='CkgSIGrD4S/tSZtV2owzpYELQz3vaUrCq5C+jqvId65xhb5OSsv3/Lwa3A8I2PY7Xpx71HaRgHFNC8CQGNp0HqC7nvYrQB+hK1HBN9SAbsIQfqQd34+6JzkkI/555IuZRX56/TccHdd/nImBERu1U39iQTbGIKW+n3+HG4tKMxUyWIXHAsyOdtMzWdN33IV2shEqE+QW4RN1yr0KnVKFzQ=='
#i1 = hexBase64_to_int(s1)
#i2 = hexBase64_to_int(s2)

