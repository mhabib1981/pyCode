import zlib
import os
from optparse import OptionParser

def main (argv)

options.add_option('-c', '--compression-level', type='int', default='2', help='compression level 1-9 (default:2)', 

if len args<1
	print options_help



input_file=open('/root/CPA_OS_Scan.txt','r').read()

if os.path.exists("/root/CPA_OS_Scan.cmp"):
	output_file=open('/root/CPA_OS_Scan.cmp','r+')
else:
	output_file=open('/root/CPA_OS_Scan.cmp','w')

x=zlib.compress(input_file, 2)
output_file.write(x)
