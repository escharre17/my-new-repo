#Exercise 2
""" fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt" 

fh = open(fname)
dixt1 = {}
for line in fh:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue
    if words[2] not in dixt1: dixt1[words[2]] = 1
    else: dixt1[words[2]] += 1
print(dixt1) """

#Exercise 3
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
print(dixt1)

#Exercise 4
max_emails = max(dixt1, key=dixt1.get)
print(max_emails, dixt1[max_emails]) """

#Exercise 5
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
lines = [line.strip('\n') for line in open(fname, 'r')
         if line.startswith('From')]
dixt1 = {}
for line in lines:
    line = line.split()
    email = line[1]
    domain = email.split('@')[1]
    dixt1[domain] = dixt1.get(domain, 0) + 1
print(dixt1)
