#!/usr/bin/python3
import random

#@number- Varible stores random numbers between -10 and 10

#It outputs the number followed by 
#the number "is positive" if the number is greater than 0
#the number "is zero" if the number is equal to 0
#the number "is negative" if the number is less than 0
#follwed by new-line

number = random.randint(-10, 10)

if (number > 0):
print(number, "is positive")
elif (number == 0):
print(number, "is zero")
else:
print(number, "is negative")
