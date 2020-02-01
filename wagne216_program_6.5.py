#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABE 651 Assignment 2
Due 1/31 17:00

Exercise 6.5from ThinkPython2 (p.61)

This is a program that prompts the user for two values 
and then computes the greatest common divisor (GCD)

@author: wagne216
"""

# Prompt user for inputs
value_1 = input('Please choose first numeric value ') # asks user for 1 no.
integer_1 = int(value_1) # converts first no. to integer
value_2 = input('Please choose a different second numeric value ') # asks for 2nd no.
integer_2 = int(value_2) # converts second no. to integer

# create system to solve for GCD
def gcd(a, b):
    r = b % a # retunrs the remainder when a/b 
    if b % r == 0 : # if there is no remainder
# print result
        return f'The greatest common divisor is {r}' 
    
# solve for GCD (greatest common divisor using the gcd function)

print(gcd(integer_1, integer_2))

