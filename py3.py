#Exercise 6
""" var2 = input("Enter Hours:", )
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
    print("Error, please enter numeric input") """

#Exercise 7
def computegrade(score):
    try:
        if(float(score) >= 0.9 and float(score) < 1.0):
            return('A')
        elif(float(score) < 0.9 and float(score) >= 0.8):
            return('B')
        elif(float(score) < 0.8 and float(score) >= 0.7):
            return('C')
        elif(float(score) < 0.7 and float(score) >= 0.6):
            return('D')
        elif(float(score) < 0.6):
            return('F')
        else:
            return('Bad Score')   
    except:
        return('Bad score')


score = input('Enter score:')
print(computegrade(score))