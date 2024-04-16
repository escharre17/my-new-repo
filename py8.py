#Exercise 1
""" fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
dixt1 = {}
for line in fh:
    words = line.split()
    if len(words) <= 2 or  words[0] != 'From': continue
    if words[1] not in dixt1: dixt1[words[1]] = 1
    else: dixt1[words[1]] += 1
list1 = [(k,v) for k, v in dixt1.items()]
list1.sort(reverse=True)
for email, count in list1[ :1]: print(email,count) """

#Exercise 2
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
dixt1 = {}
for line in fh:
    words = line.split()
    if len(words) <= 2 or  words[0] != 'From': continue
    temp = words[5].split(':')
    #print(temp[0])
    if temp[0] not in dixt1: dixt1[temp[0]] = 1
    else: dixt1[temp[0]] += 1
list1 = [(k,v) for k, v in dixt1.items()]
list1.sort()
for x, y in list1:
    print(x, y)
