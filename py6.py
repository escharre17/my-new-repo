#Exercise 1
""" fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
for x in fhand:
    print(x.upper().rstrip()) """

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
print("Done")

