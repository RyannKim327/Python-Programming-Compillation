from turtle import *

fibonacci = [0, 1]

for i in range(len(fibonacci), 15):
	x = fibonacci[i - 2]
	y = fibonacci[i - 1]
	fibonacci.append(x + y)

bgcolor("BLACK")
color("WHITE")
speed(1)

for i in range(len(fibonacci)):
	circle(fibonacci[i], 90)