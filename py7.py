#Exercise 2
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt" 

fh = open(fname)
dixt1 = {}
for line in fh:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue
    if words[2] not in dixt1: dixt1[words[2]] = 1
    else: dixt1[words[2]] += 1
print(dixt1)

#Exercise 3
""" fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
dixt1 = {}
for line in fh:
    words = line.split()
    if len(words) == 0 : continue
    if c == 'From:': continue
    #print(words)
    for c in words: 
        print(c)
        dixt1[c] = dixt1.get(c, 1) + 1
#print(dixt1) """