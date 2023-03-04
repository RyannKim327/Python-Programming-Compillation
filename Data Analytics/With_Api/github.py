import numpy
import matplotlib.pyplot as plt
import requests
import json

def getApi():
	return json.loads(requests.get("https://api.github.com/users/RyannKim327/repos").text)

languages = {}

for i in getApi():
	if languages.get(i['language']) == None:
		languages[i['language']] = 0

	languages[i['language']] += 1

keys = languages.keys()
key = []
value = []

print(keys)

for j in keys:
	if j != None and j != "None":
		key.append(j)
		value.append(languages[j])

lists = numpy.array(key)
values = numpy.array(value)

plt.xlabel("Range")
plt.ylabel("Language")

plt.plot(values)
plt.show()