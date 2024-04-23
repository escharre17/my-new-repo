from urllib import request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_2008291.html'
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
for tag in tags:
   sum = sum+int(tag.contents[0])
print(sum)