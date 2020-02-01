#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABE 651 Assignment 2
Due 1/31 17:00

Exercise 5.2 from ThinkPython2 (p.48), Part 2

This is a program that prompts user to input values for Fermat's Last Theorem (FLT), 
convert them to integers, and check if they violate the theorem

@author: wagne216


FLT: No positive integers greater than true can hold
    a^n + b^2 = c^n
"""

# 1. Prompt input values

prompt_a = input("Define a value for 'a'")
a = int(prompt_a)

prompt_b = input("Define a value for 'b'")
b= int(prompt_a)

prompt_c = input("Define a value for 'c'")
c = int(prompt_a)

prompt_n = input("Define a value for 'n'")
n = int(prompt_a)

# 2 check to see if violates theorem,and output responses whether it does or not

if n > 2:
    if a^n + b^n == c^n: # theorem statement
        print('Holy smokes, Germat was wrong!') # if true
    else:
        print("No, that doesn't work") # if not true

else: 
    print('Actually his theorem is that the exponent must be larger than 2')