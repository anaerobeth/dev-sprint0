# Hello excercise from Week 0

# Name: Elizabeth Tenorio


from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()



# This is where you put code to move bob
#move to position
def start_pos(turtle):
  pu(turtle)
  lt(turtle)
  fd(turtle, 20)
  lt(turtle)
  fd(turtle, 160)
  pd(turtle)

#write H
def write_h(turtle):
  lt(turtle)
  fd(turtle, 80)
  bk(turtle, 40)
  lt(turtle)
  fd(turtle, 40)
  lt(turtle)
  fd(turtle, 40)
  lt(turtle)
  lt(turtle)
  fd(turtle, 80)

#move to start of letter E
def letter_pos_e(turtle):
  pu(turtle)
  lt(turtle)
  fd(turtle, 20)
  lt(turtle)
  fd(turtle, 80)
  pd(turtle)

#move to start of letter L
def letter_pos_l(turtle):
  pu(bob)
  fd(bob, 20)
  lt(bob)
  fd(bob, 80)
  lt(bob)
  lt(bob)
  pd(bob)

#write E
def write_e(turtle):
  rt(turtle)
  fd(turtle, 40)
  bk(turtle, 40)
  rt(turtle)
  fd(turtle, 40)
  lt(turtle)
  fd(turtle, 40)
  bk(turtle, 40)
  rt(turtle)
  fd(turtle, 40)
  lt(turtle)
  fd(turtle, 40)

#write L
def write_l(turtle):
  fd(turtle, 80)
  lt(turtle)
  fd(turtle, 40)

#write O
def write_o(turtle):
  fd(turtle, 80)
  lt(turtle)
  fd(turtle, 40)
  lt(turtle)
  fd(turtle, 80)
  lt(turtle)
  fd(turtle, 40)

start_pos(bob)
write_h(bob)
letter_pos_e(bob)
write_e(bob)
letter_pos_l(bob)
write_l(bob)
letter_pos_l(bob)
write_l(bob)
letter_pos_l(bob)
write_o(bob)




wait_for_user()
