test=[[0,0,1,1],[1,0,0,1]]

for item in test:
	x1=item[0]
	y1=item[1]
	x2=item[2]
	y2=item[3]
	a=abs(y1-y2)
	print y1-(a*x1), y2-(a*x2)
