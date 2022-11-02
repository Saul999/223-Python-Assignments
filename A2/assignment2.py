import imp
from collections import defaultdict

from calculation import *
username = input("Enter Username: ")
print("username is: " + username) 

age = input("Enter your age: ")
print("My Age is: " + age)

print(checknumber(20))

print(finalgrade(65))

number = [20,30,40,50,70,80,90]

for val in range(len(number)):
    print(number(val))

lang = ["Python", "Java", "C", "C++"]

for itr in range(len(lang)):
    print(lang[itr].upper())

count = 0
while count < 10:
    count += 3
    print("Python while loop")

for string in "Python Loops":
    if string == "o" or string == "p" or string == "t":
        continue
    print("Current letter." + string)

for value in number:
    print("number from the list: " , value)

evencounter = 0
oddcounter = 0
for val in number:
    if(val % 2 == 0):
        evencounter += 1
    else:
        oddcounter += 1

print("count of the evens:" , evencounter)
print("count of the odds ", oddcounter)

print(range(10))

print(list(range(15)))

print(list(range(20,40)))

print(list(range(6,24,4)))



record = {'Mayer', 90, 'Sam', 95, 'Peter', 60}

def rollNo(student_name_1):
    for student in record:
        if student == '':
            return record[student]
        else:
            return "Student does not exist"


nums1 = [2,7,11,15]
nums2 = [3,2,4]

target = 9

def numfinder(nums):
    for i in nums:
         add = i + (i + 1)
         if add == target:
             return [i, i + 1]

numfinder(nums1)
number = defaultdict(int)

def twonum(nums:list[int], target int):
    number = defaultdict(int)
    for i, n in enumerate(nums):
        if target - n in number:
            return [i, number[target - n]]
            number[n] - i

result = enumerate([1,2,3])
print(result)
print(list(result))

str1 = "hello student"

str2 = "Goodmorning"

print(str[0])

a = [1, 2, 3, 4, 5, 6]

del a[0]

print(a)


tuple_1 = ("Python", "Java", "C++")


print("ele at -1 index", tuple_1[-1])

try:
    del tuple_1[1]
    print(tuple_1)
except Exception as e:
    print(e)


abs()

a = -20

print('absolute value:', abs(a))

x = 20
y = bin(20)

print(y)

test1 = []
print(test1,"is",bool[test1])


stringhe ='hello titans'
array = bytes(string, 'utf-8')
print(array)

print(callable(8))