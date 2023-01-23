import pandas
import matplotlib.pyplot as plt

file = pandas.read_csv("datas/music.csv")

file.plot(x="genre", y="age")

plt.grid()
plt.show()

print(file)