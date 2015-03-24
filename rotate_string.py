test=[[3,'forwhomthebelltolls'],[-6,'verycomplexnumber']]
x=[6,'wqumetrjxkeybsvfejargwao'],[2,'pvpklyixerigjtdiuveat'],[4,'nsfuhopwqiauiyto'],[4,'aqfdfobyoiotwny'],[-4,'cleamayluaeruybbugeeg'],[-2,'yupxoelqqqrurri'],[2,'wiiykayhxftehtawk'],[2,'alhliyuqiiwuqvnopmchrw'],[2,'ypuiklcwsoillojufe'],[-5,'ajxcrjzwccwrxiucas'],[-2,'aaajofhtastkjwosqsus'],[2,'gcmhvbxgbrhkamstme'],[-1,'isaoevamoltixouzsoo']
results=[]

for i in x:
	rot_val=i[0]
	rot_string=i[1]
	print (rot_string[rot_val:] + rot_string[:rot_val])

'''
Author's notes on this problem
Though the task could be written in a single line using cool string manipulation functions in Python and similar languages, of course it is a kind of cheating: really you are creating new string consisting of two parts of old one.

Proper challenge arose when you will try to rotate the string "in place", i.e. without creating new one, only substituting characters in it.

Good approach is to revert the string twice - around the center and then around some other point so that you will get the nicely rotated string:

Rotate by 6 letters:

initial: A B C D E F G H I J K L M N O P

1st rev: P O N M L K J I H G F E D C B A
                        ^-- center 1
2nd rev: K L M N O P A B C D E F G H I J
              ^-- center 2
'''
