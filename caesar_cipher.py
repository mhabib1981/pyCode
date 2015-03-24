alpha_set=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
x=open('ceaser_input.txt','r').readlines()
x_set=list(x)
k=1
dec_val=""

for item in x:
	for letter in item:
		if letter.lower() in alpha_set:
			enc_i=alpha_set.index(letter.lower())
			dec=alpha_set[enc_i-k]
			dec_val+=dec
		else:
			dec_val+=letter
print dec_val.upper()

new_set="" 

for i in alpha_set:
	new_set+=i.upper()
print new_set
