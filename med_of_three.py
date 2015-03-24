a=[132,8,1181,22,270,8,9,10,194,318,355,410,298,19,76,39,50,8,154,81,179,79,182,224,362,5,13,50]
b=[81,17,507,5,301,1,21,54,203,484,614,492,3,198,1054,43,31,9,7,87,39,89,168,270,823,358,15,59]
c=[1,5,10,13,967,11,110,170,35,404,621,53,1,489,960,38,134,13,57,90,172,74,64,235,352,274,12,998]
x=0

for i in a:
	if i > b[x]:
		temp=i
		if temp < c[x] and c[x] > b[x]:
			print temp
		elif temp > c[x] and c[x] > b[x]:
			print c[x]
		else:
			print b[x]
	elif i < b[x]:
		temp=b[x]
		if temp < c[x] and c[x] > i:
			print temp
		elif temp > c[x] and c[x] > i:
			print c[x]
		else:
			print i
	x+=1

'''
Author's notes on this problem
To select the middle of three elements A, B and C let us try to reorder them:

if A > B swap A with B
if B > C swap B with C
if A > B swap A with B
For swapping X and Y use the temporary variable T in three assignment, for example:

T = X; X = Y; Y = T
At the 2nd step the largest element of three would be moved to C.
After 3rd step the smallest of the remaining two is moved to A. Therefore B contains the middle element.

'''
