from turtle import *
import time

def move(x, y):
	pu()
	goto(x, y)
	pd()

title("Heart v2")
speed(1)
bgcolor("BLACK")
color("RED")
pensize(5)

move(0, -150)
left(45)
forward(150)
left(90)
forward(50)
left(45)
forward(35)
left(45)
forward(50)

right(90)
forward(50)
left(45)
forward(35)
left(45)
forward(50)
left(90)
forward(150)

time.sleep(3)