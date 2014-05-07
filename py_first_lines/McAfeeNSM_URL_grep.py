import re
import os
from urllib2 import URLError, urlopen, Request 
from optparse import OptionParser

options=OptionParser(usage='%prog [options]', description='Parse URLs from McAfeeNSM Console Raw Data')
options.add_option("-s", "--source-file", type="string", action="store", dest="filename")
opts, args = options.parse_args()
sourcefile=str(opts.filename) 
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
					url_check=http_response_check()
					#print str(url_check)
					output=refined_data.strip('\n') + ' => ' + str(url_check) + '\n'
					#http_response=urllib2.urlopen(refined_data);
					#if http_response.code == 200:
					#print refined_data
					targetfile.write(output)
	else:
		print "File Not Found!"

def http_response_check():
	with open(targetfile_name,'r') as urls:
		for url in urls:
			http_parse=Request(url)
			try:
			    http_response=urlopen(http_parse)
			except URLError, http_error:
			    return http_error.reason 
input_check()
