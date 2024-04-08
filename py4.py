#exercise 1
""" num = 0
tot = 0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    num = num + 1
    tot = tot + fval
print('All Done')
print(tot, num, tot/num) """

#exercise 2
list1 = []
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    list1.append(fval)
maxx = max(list1)
minn = min(list1)
print('All Done')
print(maxx, minn)