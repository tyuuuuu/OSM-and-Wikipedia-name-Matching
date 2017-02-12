#read content from big file

# three parameters source filename   target filename linenumber

import sys

filename1 = str(sys.argv[1])
filename2 = str(sys.argv[2])
linenumber= int(sys.argv[3])



f1 = open (filename1,"r")

f2 = open(filename2, 'w') 


i=0
for line in f1:
	i = i+1
	f2.write(line) 
	if i==linenumber:
		break
f1.close()
f2.close()



