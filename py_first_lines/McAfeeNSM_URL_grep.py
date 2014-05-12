import re
import os
import hashlib
import socket
from urllib2 import URLError, HTTPError, urlopen, Request 
from httplib import BadStatusLine
from optparse import OptionParser

#mal_analysis=load_source('wepawet_check.py', '/root/py_code/wepawet_check.py')

options=OptionParser(usage='%prog [options]', description='Parse URLs from McAfeeNSM Console Raw Data')
options.add_option("-s", "--source-file", type="string", action="store", dest="filename")
#options.add_option("-c", "--check-response", type="int", action="store", dest="verify",default=1)
opts, args = options.parse_args()
sourcefile=str(opts.filename) 
#response_check=opts.verify
targetfile_name=(sourcefile.split('/')[-1]).split('.')[0] + "_URLs"
targetfile=file(targetfile_name, 'w')
#scriptfile_name=(refined_data.split('/')[-1]).strip('\n')


def input_check():
	if sourcefile=="None":
		return options.print_help();
	else:
		grep_urls()

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
						if ".js" in refined_data:
							http_fetch(refined_data)
							hash_file=filename_gen(refined_data)
							hash_gen(hash_file)
							
						#script_file=http_fetch(output)
					
	else:
		print "File Not Found!"

def http_response_check(url):
	http_parse=Request(url)
	try:
	    http_open=urlopen(http_parse)
	except URLError as error:		
		return error.reason
	except HTTPError as  error:
		return error.reason
	except BadStatusLine as error:  
		print error
	except socket.timeout as error:
		print error


def filename_gen(url):
         scriptfile_name=(url.split('/')[-1]).strip('\n')
         return str(scriptfile_name)
		
def http_fetch(url):
        scriptfile_name=(url.split('/')[-1]).strip('\n')
	js_read=urlopen(url).read()
	script_file=file(scriptfile_name, 'w')
	return script_file.write(js_read)

def hash_gen(inFile):
	with open(inFile, 'r') as file:
		sha1_hash_gen=hashlib.sha1()
		buf=file.read(8192)
		while len(buf)> 0:
			sha1_hash_gen.update(buf)
			buf=file.read(8192)
		print sha1_hash_gen.hexdigest()
	
	
input_check()
