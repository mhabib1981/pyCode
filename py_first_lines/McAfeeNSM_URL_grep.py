import re
import os
from urllib2 import Request, urlopen, URLError
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
		response_check()

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
					refined_data="http://" + src_ip[0] + xr;
					#http_response=urllib2.urlopen(refined_data);
					#if http_response.code == 200:
						#print http_response.info()

					targetfile.write(refined_data)

	else:
		print "File Not Found!"


def response_check():
	with open(targetfile_name, 'r') as urls:
		for url in urls:
			http_parse=Request(url)
			try:
			    urlopen(http_parse)
			
			except URLError, http_error:
				print http_error.code
			
			
input_check()
