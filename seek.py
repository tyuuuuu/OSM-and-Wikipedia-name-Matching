#read content from big file
from bs4 import BeautifulSoup
import bz2

f1 = open ("enwiki-20160701-pages-articles-multistream.xml.bz2")
f2 = open("result2.xml",'w+')
start = 350231041
end = 3502418019
     


f1.seek(start)
stuff = f1.read(end - start)
stuff = bz2.decompress(stuff)
f2.write(stuff)
f2.close()




