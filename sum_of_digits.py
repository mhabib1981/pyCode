array_of_numbers=[
[97,192,138],
[217,117,86],
[394,206,4],
[39,297,23],
[333,266,36],
[13,170,91],
[282,128,75],
[147,132,168],
[67,123,33],
[396,269,133],
[249,36,61],
[128,195,139],
[296,191,76]
]

results=[]
tmp=0
for group in array_of_numbers:
	tmp=(str((group[0]*group[1])+group[2]))
	i=0
	x=0
	while not i >= len(tmp):
		x+=(int(tmp[i]))
		i+=1
	results.append(x)
print results
	
