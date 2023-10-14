import matplotlib.pyplot as plt
import numpy
import random

lists = []

for i in range(15):
	x = random.randint(0,30)
	if x in lists:
		x -= 1
	else:
		lists.append(x)

num = numpy.array(lists)

plt.xlabel("Iteration")
plt.ylabel("Given random numbers")

plt.plot(num)
plt.grid()
plt.show()