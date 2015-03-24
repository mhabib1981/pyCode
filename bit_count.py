test=[1,100,1000,44,-1000,-1,-1234]
x=[1473,-87888240,-268742519,-170704066,-153020132,-8349893,-593677,12366746,-93736318,14,-19860848,-162174260,155,126,93,-3674,15406260,-933895,6048072,-78890,141135005,18,24381,-3382,-743415790,1457,10,-2,17637964,-82188537,6914046,84499,16,909737,796685,-135,141236432,-1570,-106,-8247,2,-13401071,1700,884155173,-147243,-4186632,-65873,629498343,10434,-19124866,2555,1523782,-1]
results=[]

def calc_rem_pos(decimal):
	tmp=decimal
	rem=0
	bin_vals=""
	while not tmp == 0:
		rem=tmp%2
		tmp=tmp/2
		if rem == 1:	
			bin_vals+=str(rem)
	results.append(len(bin_vals))

def calc_rem_neg(decimal):
	'''
	the trick here to minus 1 from the decimal number so you can get 
	the exact binary representation if the value is inversed 0's to 1's
	and vice versa, by counting total of bit 1 and sunstratcting it
	from the length stated (32) we get the exact count of 1's bits.
	'''
        tmp=abs(decimal)-1
        rem=0
        bin_vals=""
        while not tmp == 0:
                rem=tmp%2
                tmp=tmp/2
                if rem == 1:
                        bin_vals+=str(rem)
        results.append(32-len(bin_vals))


def main():
	for number in x:
		if number > 0:
			calc_rem_pos(number)
		elif number < 0:
			 calc_rem_neg(number)
	print results
	
if __name__=='__main__':
	main()
