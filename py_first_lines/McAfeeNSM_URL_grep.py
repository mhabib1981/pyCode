import re
import os
from urllib2 import URLError, urlopen, Request 
from optparse import OptionParser

options=OptionParser(usage='%prog [options]', description='Parse URLs from McAfeeNSM Console Raw Data')
options.add_option("-s", "--source-file", type="string", action="store", dest="filename")
#options.add_option("-c", "--check-response", type="int", action="store", dest="verify",default=1)
opts, args = options.parse_args()
sourcefile=str(opts.filename) 
#response_check=opts.verify
targetfile_name=(sourcefile.split('/')[-1]).split('.')[0] + "_URLs"
targetfile=file(targetfile_name, 'w')

def input_check():
	if sourcefile=="None":
		return options.print_help();
	else:
		grep_urls()
		#http_response_check()

def grep_urls():
	if os.path.exists(sourcefile):
		raw_data=open(sourcefile, 'r').readlines();
		for line in raw_data:
			if "HTTP URI" in line:
				ip_pattern=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
				src_ip=re.findall(ip_pattern, line)
				xl=re.sub(r'^(.*)HTTP URI == ',"",line);
	                	xr=re.sub(r';(.*)',"",xl);
				if "n/a" not in xr:
					refined_data="http://" + src_ip[0] + xr
					query=http_response_check(refined_data)
					if "None" in str(query):
						targetfile.write(refined_data)
						http_fetch(refined_data)
						#print output
						#script_file=http_fetch(output)
						#print script_file
					#targetfile.write(output)
	else:
		print "File Not Found!"

def http_response_check(url):
	http_parse=Request(url)
	try:
	    http_open=urlopen(http_parse)
	except URLError, http_error:
		return http_error.reason
	
def http_fetch(url):
	if ".js" in url:
		js_read=urlopen(url).read()
		scriptfile_name=(url.split('/')[-1]).strip('\n')
		script_file=file(scriptfile_name, 'w')
		return script_file.write(js_read)

input_check()
