import re
#exercise 1
expression = input("Enter a refular expression:")

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox.txt"


count = 0
fh = open(fname)
for line in fh:
    words = line.split()
    for word in words: 
        y = re.findall(expression, word)
        if len(y) > 0:
            count = count + 1
print('mbox.txt had', count, 'lines that matched', expression )