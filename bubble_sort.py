x=[1,10,14,9,18,3,16,4,17,13,12,8,15,2,7,6,11,5]
p=0
s=0

n=len(x)
while not n==0:
	nx=0
	for i in range(1,n):
		if x[i-1] > x[i]:
			tmp=x[i-1]
			x[i-1]=x[i]
			x[i]=tmp
			nx=i
			s+=1
	n=nx
	p+=1
print x,p,s		

