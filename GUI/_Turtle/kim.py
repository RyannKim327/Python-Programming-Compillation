from turtle import *

a = 300
b = 1.5

k = -300
i = -100
m = -50

def place(x, y):
	pu()
	goto(x, y)
	pd()

def place2(x):
	pu()
	forward(x)
	pd()

speed(1)
color("white")
bgcolor("black")

place(k, 0)

left(90)
forward(a)

place(k, a / 2)

right(45)
forward(a / b)

place(k + 25, a / 1.8)

right(100)
forward(a / b)

place(i, 0)

left(145)
forward(a / 2)

place(i, (a - (a / 3)))

forward(10)

place(m, 0)

forward(a / 2)

right(90 + 45)
forward(a / 3)

left(90)
forward(a / 3)

right(90 + 45)
forward(a / 2)

place2(10)

goto(k, -10)