# Name: Saul Ruiz
# Date: 08/24/2022
# File Purpose: Multiple hello functions

def helloworld():
    return "Hello World!"

def helloname(name):
    return "Hello " + name + "!"

def club():
    dct = dict()
    dct['str'] = "AppDivided"
    dct['age'] = 3
    return dct

def division(a, b):
    return a / b

def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def mult(a, b):
    return a * b

def operations(a, b):
    add = a + b
    sub = a - b
    multiply = a * b
    division = a / b
    return add, sub, multiply, division

def factorial(a):
    ans = a % 2
    if(ans == 1):
        return("odd")
    else:
        return("even")
    