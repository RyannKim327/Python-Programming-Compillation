import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

file = pandas.read_csv("data/music.csv")
_x = file.drop(columns=["genre"])
_y = file['genre']
xtrain, xtest, ytrain, ytest = train_test_split(_x, _y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(xtrain, ytrain)
predictions = model.predict(xtest)

sc = accuracy_score(ytest, predictions)

print(predictions)
print(sc)