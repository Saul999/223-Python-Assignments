def checknumber(num):
    if(num < 0):
        return("Number is negative")
    elif(num == 0):
        return("Number is Neutral")
    elif(num > 0):
        return("Number is Positive")
    else:
        return("Number is not Fit in the given condition")


def finalgrade(percent):
    if(percent >= 90):
        return("Congrats! You got an A")
    elif(percent < 90 & percent >80):
        return("You got a B")
    elif(percent < 80 & percent > 70):
        return("You got a C")
    elif(percent < 70 & percent > 60):
        return("You got a D")
    else:
        return("sadly you got a F")

def checkcircle(num):
    if num < 0:
        return "Number is Negative"
    elif num == 0:
        return "Number is neutral "
    elif num > 0:
        return "Number is psotive"
    else:
        return "nothing"

def areaCicle(radius):
    return radius * 3.14


