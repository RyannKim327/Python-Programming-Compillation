from turtle import *

def place(x, y):
	pu()
	goto(x,y)
	pd()

def placeX(x):
	pu()
	forward(x)
	pd()

def draw(x):
	forward(x)

speed(1)
color("white")
bgcolor("black")

center = 0

place(center - 150, center - 150)
left(75)
draw(300)

right(75 + 75)
draw(300)

right(75 + 75)
draw(300)

right(135)
draw(255)

right(132)
draw(300)
