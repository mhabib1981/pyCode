import re

input_file=open('/root/sp_safari_image_element_290414.txt', 'r')
data=input_file.readlines()
#output_file=open('/root/sp_safari_clean_urls', 'r+')
for line in data:
	if "HTTP URI" in line:
		xl=re.sub(r',(.*)HTTP URI == ',"",line);
		xr=re.sub(r';(.*)',"",xl);
			
		if "n/a" not in xr:
			print "<img src=\"http://" + xr.strip("\n") + " " + "\"id=\"i\">"
			
			
input_file.close()
