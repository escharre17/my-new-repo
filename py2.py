#Exercise 1
""" var2 = float(input("Enter Hours:", ))
var3 = float(input("Enter Rate:", ))
if (var2 > 40):
    over = (var2 - 40) * (var3 + (var3/2))
    pay = over + var2*var3
else:
    pay = var2*var3 

print("Pay:", pay)
 """
#Exercise 2
var2 = input("Enter Hours:", )
var3 = input("Enter Rate:", )
try:
    var2 = float(var2)
    var3 = float(var3)
    if (var2 > 40):
        over = (var2 - 40) * (var3 + (var3/2))
        pay = over + var2*var3
    else:
        pay = var2*var3 
    print("Pay:", pay)
except:
    print("Error, please enter numeric input")

#Exercise 3
score = input('Enter score:')

try:
    if(float(score) >= 0.9 and float(score) < 1.0):
        print('A')
    elif(float(score) < 0.9 and float(score) >= 0.8):
        print('B')
    elif(float(score) < 0.8 and float(score) >= 0.7):
        print('C')
    elif(float(score) < 0.7 and float(score) >= 0.6):
        print('D')
    elif(float(score) < 0.6):
        print('F')
    else:
        print('Bad Score')   
except:
    print('Bad score')