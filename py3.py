#Exercise 6
def computepay(h, r):
    try:
        if (h > 40):
            over = (h - 40) * (r + (r/2))
            pay = over + h*r
            return pay
        else:
            pay = h*r 
            return pay
    except:
        print("Error, please enter numeric input")

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