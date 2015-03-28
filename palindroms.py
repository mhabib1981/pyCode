#!/usr/bin/python
test=("Stars","O, a kak Uwakov lil vo kawu kakao!","Some men interpret nine memos")

for item in test:
	i=0
	while not i==len(item)-1:
		if item[i] == item[len(item)-1]:
			print "Y"
		else:
			print "N"
	i+=1
