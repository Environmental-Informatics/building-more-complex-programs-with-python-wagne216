#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABE 651 Assignment 2
Due 1/31 17:00

Exercise 4.2 from ThinkPython2 (p.37)

Set of functions that use the turtle module to draw 
3 different flowers shown in Fig. 4.1
@author: wagne216
"""

#t.clear() # comment out first round
import turtle 
from math import *

# start with a turtle
t = turtle.Turtle()
c = "black" # define intial color

# use an arc to draw circle pieces
def arc(t, rad, no_sides, angle):
#    t = turtle.Turtle()
# the number of iterations depends on the angle:    
    for i in range(int(no_sides*angle/360)):
# length of forward movement = arc length
        t.fd(2*pi*rad/no_sides) # moves turtle
# color
        t.pencolor(c)
        t.fillcolor(c)
# degree turn after each line segment depends on input numbers of sides
        t.rt(360/no_sides)


# Execute these commands in sequence
# to draw each of the 3 flowers:


def shape(n_petals, angle, rad): # each flower uses arc function which can be generalized

    for i in range(n_petals):       
        arc(t, rad, 80, angle)
        # after each arc drawn, rotate before drawing next:
        t.rt(180-angle) # turn back around to complete petal
        arc(t, rad, 80, angle)
        t.rt(360/n_petals +(180-angle))

# start at left of screen
t.pu()
t.setpos(-200,0)
t.pd()
# flower 1 
shape(7, 60, 100)

# move to next location
t.pu()
t.setpos(0,0)
t.pd()

# flower 2 
shape(10, 55, 100)

# move to next location
t.pu()
t.setpos(200,0)
t.pd()

# flower 3 
shape(20, 20, 150)
