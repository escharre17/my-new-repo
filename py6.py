
#Exercise 2
fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
out = -1
numbers =[]
for x in fhand:
    out = x.find('X-DSPAM-Confidence:')
    if out != -1:
        number = float(x[(len(out)+out):(out + x.find(' '))])
        numbers.append(number)
        count = count + 1
avg1 = sum(numbers)/len(numbers)
