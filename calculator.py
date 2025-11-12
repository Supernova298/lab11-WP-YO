# https://github.com/Supernova298/lab11-WP-YO
# Partner 1: Will Parkin
# Partner 2: Yancho Ovcharov
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

def square_root(a):
    if a < 0:
        raise ValueError()
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a,b)


def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError()
    else:
        return b / a

def logarithm(a, b):
    if a == 0 or b == 0:
        raise ValueError()
    else:
        return math.log(b, a)

def exp(a, b):
    return a ** b
