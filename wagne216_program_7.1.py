#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABE 651 Assignment 2
Due 1/31 17:00

Exercise 6.5 from ThinkPython2 (p.69)

This is a program that produces a table similar to that shown on pg. 69

@author: wagne216
"""
from math import * # to get sqrt function

# 1. define funciton retunrs squrae root using logic fr. 7.5 (Newton's method)
threshold = 1e-16
#x = 0
def mysqrt(a):
    x = 3 # initial guess
    while True: # loop forever as long as estimate not close enough
#        print(x) # every round of x will be printed until final answer
        y = (x + a/x)/2 # new iterative estimate 
#       when close enough
        if abs(y-x) < threshold:
            return x
            break
        x = y

# 2. function that prints table comparing real and approx sqr root outputs
def test_square_root(i):
    print('                                   ') # make blank space before table
    print('a  ','mysqrt(a)    ','math.sqrt(a) ','diff') # header
    print('-  ','---------    ','------------ ','----') # header underline

    for j in range(1,i):
        # spceify no. decimal places
        print("%.1f" % j, "%.11f" % mysqrt(j), "%.11f" % sqrt(j), "%.11f" % abs(sqrt(j)-mysqrt(j))) # each row in table
 
# execute:               
test_square_root(10)