#Exercise 2
fname = input("Enter file name: ")
""" if len(fname) < 1:
    fname = "mbox-short.txt" """

fh = open(fname)
dixt1 = {}
for line in fh:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From:' : continue
    for c in words:
        if c == 'From:': continue
        dixt1[c] = dixt1.get(c, 0) + 1
print(dixt1)
print()
