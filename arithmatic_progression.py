x=[
[26,0,85],
[2,7,16],
[26,16,16],
[10,16,61],
[30,11,94],
[18,3,33],
[1,15,39],
[21,9,60],
[15,8,69],
[9,14,20]
]


results=[0]*len(x)
i=0

for item in x:
	a=item[0]
	b=item[1]
	n=item[2]
	tmp=0
	while not n==0:
		tmp+=a+b*(n-1)
		n-=1
	results[i]=tmp
	i+=1
	
print results
		

	
	
