'''
x='123'
a=list(x)
y=[]
i=0
k=0

while i < len(y):
	k*=10
	k+=y[i]
	i+=1
print k
'''

x='123'
k=0

#Converting into Integers by refering to ascii table value

for i in x:
	k=ord(i) - 48
	print k
