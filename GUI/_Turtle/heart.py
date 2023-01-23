from turtle import *
import time

def move(x, y):
	pu()
	goto(x, y)
	pd()

title("Heart")
pen("Heart")
speed(1)
bgcolor("BLACK")
color("RED")
pensize(5)

move(0, -100)
left(55)
forward(150)
circle(50, 190)
forward(33)

move(0, -100)

right(110)
forward(150)
circle(-50, 190)
forward(33)

move(0, 0)

time.sleep(3)