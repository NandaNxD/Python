import xml.etree.ElementTree as ET
import urllib.request,urllib.response,urllib.request
import xml.etree.ElementTree as ET
import re
#http://py4e-data.dr-chuck.net/comments_42.xml
url=input('Enter Location ')
print('Retrieving '+url);
data=urllib.request.urlopen(url).read()

print("Retrieved "+str(len(data))+" characters")
tree=re.findall('<count>([0-9]+)</count>',str(data.decode()))
d=ET.fromstring(data)
s=0
cnt=0
for n in tree:
    cnt+=1;
    s+=int(n)
print('Count '+str(cnt))
print('Sum '+str(s))
