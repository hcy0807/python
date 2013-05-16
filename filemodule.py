def readfile(s):
	try:
		content = open(s);
	except IOError,e:
		print "open file error",e
	else:
		for i in content:
			print i

