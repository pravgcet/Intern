#Created By : Praveen Kumar
#Contact : +91 9717811031 , pravgcet@gmail.com	

import os
import re
import sys,getopt

def traverse(path):

	pattern1 = r"[+][9][1] [9|8|7][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9](\D)"
	pattern2 = r"[+][9][1][9|8|7][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9](\D)"
	pattern3 = r"[9|8|7][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9](\D)"
	
	re.escape(pattern1)
	re.escape(pattern2)

	for dirpath, dirs, files in os.walk(path):
		for fl in files:
			f=open(dirpath+"/"+fl)
			for ln in f:
				obj1=re.match(pattern1,ln)
				obj2=re.match(pattern2,ln)
				obj3=re.match(pattern3,ln)
				if obj1:
					print obj1.group(0)[4:]
				elif obj2:
					print obj2.group(0)[3:]
				elif obj3:
					print obj3.group(0)
					
			f.close()


if __name__=="__main__":
	traverse(sys.argv[1])	













