#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add

result = add(a, b)
print('{} + {} = {}'.format(a, b, result))

a = 10
b = 5
from calculator_1.py import sub

result = sub(a, b)
print('{} + {} = {}'.format(a, b, result))

a = 10
b = 5
from calculator_1.py import mul

result = mul(a, b)
print('{} + {} = {}'.format(a, b, result))

a = 10
b = 5
from calculator_1.py import div

result = div(a, b)
print('{} + {} = {}'.format(a, b, result))
