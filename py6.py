""" #Exercise 1
fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
for x in fhand:
    print(x.upper().rstrip())

#Exercise 2
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        pos = line.find(':') +1
        num = line[pos:]
        print(num)
    print(line)
print("Done") """

#Exercise 3
""" fname = input("Enter file name: ")
fh = open(fname)
lst1 = []
lst = []
for line in fh:
    line.strip()
    word = line.split()
    lst1.append(word)
for x in lst1:
    for n in x:
        lst.append(n)
lst.sort()
print(lst) """

#Exercise 4
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From:' : continue
    count = count + 1
    print(words[1])
    
print("There were", count, "lines in the file with From as the first word")

