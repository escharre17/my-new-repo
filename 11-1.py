import re

fname = ('regex_sum_2008289.txt')
sum_lst = 0
fh = open(fname)
for line in fh:
    words = line.split()
    for word in words: 
        y = re.findall('[0-9]+', word)
        if not y: continue
        else:
            for x in y:
                sum_lst +=int(x)

print(sum_lst)

