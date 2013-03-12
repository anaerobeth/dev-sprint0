# Flower excercise (4.2) from Week 0

# Name: Elizabeth Tenorio

import math
from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

# This is where you put code to move bob

def polyline(turtle, length, angle, n):
    for i in range(n):
        fd(turtle, length)
        lt(turtle, angle)
#polyline(bob, 50, 20, 5)

def arc(turtle, radius, theta):
    circumference = 2 * 3.1416 * radius
    arc_length = radius * math.radians(theta)
    n = int(circumference / 3) + 1
    step_length = arc_length / n
    step_angle = float(theta) / n
    polyline(turtle, step_length, step_angle, n)

#arc(bob, 50, 100)


def petal(turtle, radius, angle):
    for i in range(2):
        arc(turtle, radius, angle)
        lt(turtle, 180 - angle)

#petal(bob, 100, 80)
def flower(turtle, p, radius, angle):
    for i in range(p):
        petal(turtle, radius, angle)
        lt(turtle, 360.0/p)

def position(turtle, length):
    pu(turtle)
    fd(turtle, length)
    pd(turtle)

position(bob, -100)
flower(bob, 7, 80.0, 60.0)

position(bob, 180)
flower(bob, 10, 60.0, 80.0)

position(bob, 180)
flower(bob, 20, 120.0, 20.0)


wait_for_user()

