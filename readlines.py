import sys

filename1 = str(sys.argv[1])




f1 = open (filename1,"r")



i=0
for line in f1:
	i = i+1

print i
f1.close()

