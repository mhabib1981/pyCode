test=[[2,3],[4,10]]
x=[[1224,3026],[9,3092],[4872,9],[5,285],[2900,3364],[4750,5],[63,715],[321,5],[768,912],[10,348],[1943,1972],[2,986],[4677,28],[9108,920],[777,3256],[5546,3658],[1416,2400],[1987,7]]
results=[]

for i in x:
	dvn=i[0]
	div=i[1]
	quo=dvn/div
	rem=dvn%div
	while not rem==0:
		dvn=div
		div=rem
		quo=dvn/div
		rem=dvn%div
	gcd=div
	lcm=(i[0]*i[1]) / gcd
	results.append(gcd)
	results.append(lcm)

#print results

	print  ("(" + str(gcd) + " " + str(lcm) + ")")
