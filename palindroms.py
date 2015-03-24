#!/usr/bin/python
ltest=("Stars","O, a kak Uwakov lil vo kawu kakao!","Some men interpret nine memos")
results=[0]*len(test)

for i in test:
	found=False
	c=test.index(i)
	if not " " in i:
		ix=i.lower()
		if ix[0] == ix[-1] and ix[1] == ix[-2]:
			results[c]="Y"
		else:
			results[c]="N"
	else:
		test_case=i.split(" ")
		for i in test_case:
			ix=i.lower()
			if len(i)>2 and ix[0] == ix[-1] and ix[1] == ix[-2] and found==False:  			
				results[c]="Y"
				found=True
			else:
				results[c]="N"
			
		
print results
