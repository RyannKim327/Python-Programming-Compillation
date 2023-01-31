import pandas
import matplotlib.pyplot as plot

file = pandas.read_csv("datas/gh-push-event.json.csv")
file.plot(x="name", y="count")

plot.grid()
plot.show()