from urllib import request
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_2008293.xml'
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
comment = tree.findall('comments/comment')
count=len(comment)
sum=0

for i in comment:
    sum += float(i.find('count').text)
print(count)
print(sum)