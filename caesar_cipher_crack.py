inFile=open('caesar_input.txt','r').readlines()
outFile=file('caesar_output.txt','rw+')
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
freq_letters='ESTDNRYFLOGHAKMPUW'
common_words=['of','to','in','it','is','be','as','at','so','we','he','by','or','on','do','if','me','my','up','an','go','no','us','am']
alpha_set=list(alpha)
rep_count={}

def get_max(x):
	for letter in alpha_set:
		i=alpha_set.index(letter)
		rep_count[i]=(x.count(letter))
		max_val=max(rep_count.values())
	return max_val


def get_key(value,alpha):
	for key in rep_count:
		if rep_count[key]==value:
			key_val=abs(key-alpha_set.index(alpha))
			return key_val

def dec_text(input,key):
	tmp=''
	for char in input:
		if char in alpha_set:
			i=alpha_set.index(char)
			tmp+=alpha_set[i-key]
		else:
			tmp+=char
	return tmp

def check_common(tmp_set):
        for word in tmp_set:
                if len(word) == 2 and word.lower() in common_words:
                        return False

def main():
	for line in inFile:
		x=line.strip('\n')
		max_val=get_max(x)
		check_alpha=True
		for alpha in freq_letters:
			key_val=get_key(max_val,alpha)
			tmp=dec_text(x,key_val) + " using "+ alpha  + str(key_val) + "\r\n"
			tmp_set=tmp.split(" ")
			if check_common(tmp_set) == False:
				print tmp

if __name__ == '__main__':
	main()
