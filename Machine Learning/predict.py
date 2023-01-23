import pandas
from sklearn.tree import DecisionTreeClassifier

file = pandas.read_csv("data/music.csv")

drop = file.drop(columns=["genre"])
y = file['genre']

decision = DecisionTreeClassifier()

decision.fit(drop.values, y.values)

# You may also use this format
# decision.fit(drop, y)
# But it gives you a warn

# format [age, gender]
model = decision.predict([ [21, 1], [22, 0] ])
print(f"21 year old male wants {model[0]} and 22 year old female wants {model[1]}")