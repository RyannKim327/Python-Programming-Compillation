import matplotlib.pyplot as plt
import requests
import json

def fetch():
	return json.loads(requests.get('https://api.github.com/users/RyannKim327/repos?per_page=1000').text)

langs = {}

for i in fetch():
	if i['language'] == None:
		i['language'] = "None"
	if langs.get(i['language']) == None:
		langs[i['language']] = 0
	langs[i['language']] += 1

print(langs)

plt.xlabel = "Languages"
plt.ylabel = "Counts"

plt.bar(x=range(len(list(langs.keys()))), width=1, height=langs.values())
plt.xticks(range(len(list(langs.keys()))), list(langs.keys()))
plt.grid()
plt.show()