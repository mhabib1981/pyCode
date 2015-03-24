x=[2103,1724,405,43697,624,3885,427,1794,486,290,31,43,245,411,131,500,4163,54,799,8326,264]
steps=[0]*21

for number in x:
	i=x.index(number)
	tmp=number
	while not tmp ==1:
		if tmp % 2 == 0:
			tmp=tmp/2
			steps[i] +=1

		else:
			while not tmp % 2 == 0:
				tmp=tmp*3+1
				steps[i] +=1

print steps
