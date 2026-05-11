''' OBJECTS
    (1) What is object
    (2) Interable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''


import array # package/module
import math # package
from math import ceil
print("======= What is object =======")
# An object has state and method properties
# Everything is object in Python

print(type('Hello World'))
print(type(1000))
print(type(True))
print(type(array))
print(type(math))

# Paragidm > Functional Programming & OOP
# OOP 4 concepts > Abstaction | Encapsulation | Inheritance | Polymorphism
result1 = math.ceil(97.7) #CALL
print("result1:", result1)

result2 = math.ceil(98.7) #ceil
print("result2:", result2)