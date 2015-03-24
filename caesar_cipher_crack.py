inFile=open('caesar_input.txt','r').readlines()
outFile=file('caesar_output.txt','rw+')
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
freq_letters='ESTDNRYFLOGHAKMPUW'
common_words_2=['of','to','in','it','is','be','as','at','so','we','he','by','or','on','do','if','me','my','up','an','go','no','us','am']
common_words_3=['the','and','for','are','but','not','you','all','any','can','had','her','was','one','our','out','day','get','has','him','his','how','man','new','now','old','see','two','way','who','boy','did','its','let','put','say','she','too','use']
common_words_4=['that','with','have','this','will','your','from','they','know','want','been','good','much','some','time']
alpha_set=list(alpha)
rep_count={}

def get_max(x):
	for letter in alpha_set:
		i=alpha_set.index(letter)
		rep_count[i]=(x.count(letter))
	return max(rep_count.values())
	

def get_key(value,alpha):
	for key in rep_count:
		if rep_count[key]==value:
			return abs(key-alpha_set.index(alpha))

def dec_text(input,key):
	tmp=''
	for char in input:
		if char in alpha_set:
			i=alpha_set.index(char)
			tmp+=alpha_set[i-key]
		else:
			tmp+=char
	return tmp

def check_common_2(tmp_set):
        for word in tmp_set:
		if len(word) == 2 and word.lower() in common_words_2:				
			return False

def check_common_3(tmp_set):
        for word in tmp_set:
                if len(word) == 3 and word.lower() in common_words_3:
                        return False

def check_common_4(tmp_set):
        for word in tmp_set:
                if len(word) == 4 and word.lower() in common_words_4:
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
			if check_common_2(tmp_set) == False and check_common_3(tmp_set)==False and check_common_4(tmp_set)==False:
				print "Certainity Level: 99% --> " + tmp
			elif check_common_2(tmp_set)==False and check_common_3(tmp_set)==False:
				print "Certainity Level: 66% --> " + tmp
			elif check_common_2(tmp_set)==False:
				print "Certainity Level: 33% --> " + tmp

if __name__ == '__main__':
	main()
