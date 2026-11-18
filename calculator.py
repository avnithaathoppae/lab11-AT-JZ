"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def logarithm(a, b):
    if b<=0 or a<=0 or a==1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def add(a, b):
   return a + b


def sub(a, b):
   return a - b


def mul(a, b):
   return a * b


# raise ZeroDivisionError if a == 0
def div(a, b):
   if a == 0:
       raise ZeroDivisionError("Error. Cannot divide by zero")
   return b / a


# use math library + raise ValueError
def log(a, b):
   try:
       return math.log(b, a)
   except:
       raise ValueError("Error. Invalid logarithm arguments")


def exp(a, b):
   return a ** b

