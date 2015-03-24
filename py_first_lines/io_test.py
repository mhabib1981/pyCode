import os
sourcefile=('/root/Hello.txt')

if os.path.exists(sourcefile):
	data=open(sourcefile).readlines()
	print data
else:
	print "Error!"
