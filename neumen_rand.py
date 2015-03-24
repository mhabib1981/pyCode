test=[0001,4100,5761]
x=[2663,4514,6716,9511,3416,9251,5889,3488,9232,5538,9388,1687,8785,5546]
results=[]

def num_power(number):
	tmp_pow=number ** 2
	return num_len(tmp_pow)

def num_truncate(number):
	tmp_truncate=number / 100
	tmp_truncate=tmp_truncate % 10000
	return tmp_truncate

def num_len(number):
	str_num=str(number)
	while not len(str_num) == 8:
		tmp_len= '0' + str_num
		str_num=tmp_len
	return  num_truncate(int(str_num))

def main():
	for number in x:
		c=0
		tmp_vals=[]
		tmp=number
		tmp_vals.append(tmp)
		while not tmp_vals.count(tmp) > 1:
			tmp=num_power(tmp)
			tmp_vals.append(tmp)
			c+=1
		results.append(c)
	print results
						

if __name__=='__main__':
	main()
