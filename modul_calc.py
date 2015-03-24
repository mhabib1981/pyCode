test='7 * 41 + 1 * 4242 * 82 * 5 + 8 * 4 * 585 + 2785 + 4 * 766 * 9 + 594 + 558 * 1589 + 3 * 3393 + 1 * 83 * 9 * 6 + 72 + 3954 + 296 + 3 * 37 * 4 * 6 * 8890 * 9904 + 6 * 51 + 34 * 9623 * 22 + 5 * 55 + 752 + 8 + 69 + 2 * 5 * 87 * 8 + 3 * 503 + 8 * 43 % 1516'
xtest=test.split(" ")
sign=['+']
number=[]
result=0
k=0
c=0

for item in xtest:
	i=xtest.index(item)
	if i % 2 == 0:
		number.append(int(xtest[i]))
	else:
		sign.append(xtest[i])

print sign
print number

while not sign[c] == '%':
	if sign[c] == '+':
		k+=number[c]
		c+=1

	elif sign[c] == '*':
		k*=number[c]
		c+=1
	
result= k % number[-1]
print result
