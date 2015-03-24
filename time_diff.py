x=[
[19,3,55,49,23,11,24,7],
[5,21,36,8,12,3,1,1],
[4,1,29,47,9,8,32,10],
[15,21,10,34,17,8,38,11],
[5,6,41,22,12,2,5,49],
[11,12,54,27,13,8,5,32],
[3,3,19,15,25,4,16,4],
[5,7,46,4,8,7,11,23],
[4,11,7,51,21,9,43,32],
[15,14,18,2,25,11,36,15],
[19,22,16,13,25,13,26,16],
[9,18,1,6,18,20,7,56]
]


def diff_in_sec(item):
	days=item[0]*24*3600,item[4]*24*3600
	hrs=item[1]*3600,item[5]*3600
	min=item[2]*60,item[6]*60
	sec=item[3],item[7]
	val_a=(days[0]+hrs[0]+min[0]+sec[0])
	val_b=(days[1]+hrs[1]+min[1]+sec[1])
	diff_sec=val_a - val_b
	return abs(diff_sec)

def convert_to_time():
	for i in x:
		tmp=0
		diff=diff_in_sec(i)
		days=diff/ (24*3600)
		tmp=diff % (24*3600)
		hrs=tmp / 3600
		tmp=tmp % 3600
		min=tmp / 60
		tmp=tmp % 60
		sec=tmp
		results=days,hrs,min,sec
		print results

convert_to_time()
