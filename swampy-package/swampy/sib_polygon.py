# Polygon excercise from Week 0

# Name: Elizabeth Tenorio

import math
from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()



# This is where you put code to move bob
def square():
    for i in range(4):
        fd(bob, 100)
        lt(bob)

#square()


# This is the generalized function that takes a turtle and a length
def square(turtle, length):
    for i in range(4):
        fd(turtle, length)
        lt(turtle)

# square(bob, 50)

# This is the generalized function that takes an additional parameter
def polygon(turtle, length, n):
    angle = 360.0/n
    for i in range(n):
        fd(turtle, length)
        lt(turtle, angle)

#polygon(bob, 50, 6)

# This is the simple function to draw a circle
def circle(turtle, radius):
    circumference = 2 * 3.1416 * radius
    n = 360
    length = circumference / n
    polygon(turtle, length, n)

#circle(bob, 100)

# This is the simple function to draw an arc
def arc(turtle, radius, theta):
    circumference = 2 * 3.1416 * radius
    n = 360
    length = circumference / n
    angle = 360.0/n
    for i in range(theta):
        fd(turtle, length)
        lt(turtle, angle)
#arc(bob, 100, 100)

# This is an altenative function to draw a circle
def circle_alt(turtle, radius):
    circumference = 2 * 3.1416 * radius
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(turtle, length, n)

#circle_alt(bob, 100)

# This is an altenative function to draw an arc
def arc_alt(turtle, radius, theta):
    circumference = 2 * 3.1416 * radius
    arc_length = radius * math.radians(theta)
    n = int(circumference / 3) + 1
    step_length = arc_length / n
    step_angle = float(theta) / n

    for i in range(n):
        fd(turtle, step_length)
        lt(turtle, step_angle)

#arc_alt(bob, 100, 100)

# This is the refactored function to draw a shape
def polyline(turtle, length, angle, n):
    for i in range(n):
        fd(turtle, length)
        lt(turtle, angle)
#polyline(bob, 50, 20, 5)

# This is the refactored function to draw a polygon
def polygon2(turtle, length, n):
    angle = 360.0/n
    polyline(turtle, length, angle, n)
#polygon2(bob, 100, 5)

# This is the refactored simple function to draw a circle
def circle2(turtle, radius):
    circumference = 2 * 3.1416 * radius
    n = 360
    length = circumference / n
    angle = 360.0 / n
    polyline(turtle, length, angle, n)
#circle2(bob, 100)

# This is the refactored simple function to draw an arc
def arc2(turtle, radius, theta):
    circumference = 2 * 3.1416 * radius
    n = 360
    length = circumference / n
    angle = 360.0/n
    polyline(turtle, length, angle, theta)
#arc2(bob, 100, 180)


# This is the refactored alternative function to draw a circle
def circle2_alt(turtle, radius):
    circumference = 2 * 3.1416 * radius
    n = int(circumference / 3) + 1
    length = circumference / n
    angle = 360.0 / n
    polyline(turtle, length, angle, n)


# This is the refactored alternative function to draw an arc
def arc2_alt(turtle, radius, theta):
    circumference = 2 * 3.1416 * radius
    arc_length = radius * math.radians(theta)
    n = int(circumference / 3) + 1
    step_length = arc_length / n
    step_angle = float(theta) / n
    polyline(turtle, step_length, step_angle, n)

#arc2_alt(bob, 50, 100)

#how to draw a circle with the turtle as the center
"""
pu(bob)
fd(bob, 50)
lt(bob)
pd(bob)
circle2(bob, 50)
pu(bob)
lt(bob)
fd(bob, 50)
lt(bob, 180)
pd(bob)
"""


wait_for_user()
