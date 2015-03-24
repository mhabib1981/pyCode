a=[57,85,117,55,68,60,89,54,87,98,83,62,51,89,57,67,86,113,118,42,111,97,90,41,59,71,112,59,86]
b=[1.83,1.92,3.12,1.51,1.48,1.69,2.11,1.47,2.09,2.56,2.35,1.64,1.21,1.57,1.69,1.75,1.57,2.13,3.01,1.49,2.48,2.01,1.63,1.60,1.40,1.49,1.97,2.32,1.59]
y=[]
result=[]

x=0

for i in a:
	y.append(round(i/(b[x]**2),2))
	x+=1

for i in y:
	if i < 18.50:
		result.append("under")
	elif i >= 18.50 and i < 25.0:
		result.append("normal")
	elif i >= 25.0 and i < 30.0:
		result.append("over")
	elif i >= 30.0:
		result.append("obese")
print result

print y
