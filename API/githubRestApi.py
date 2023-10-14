import requests as req
import json

def typing(txt):
	l = 75000
	i = len(txt) * l
	j = 0
	while j < i:
		if(j % l) == 0:
			print(txt[j // l], end="", flush=True)
		j += 1
	print()

def usr(usn):
	r = req.get(f'https://api.github.com/users/{usn}/repos').text
	j = json.loads(r)
	return j

def repo(usn, name):
	r = req.get(f'https://api.github.com/repos/{usn}/{name}').text
	j = json.loads(r)
	return j

usn = input("Enter username: ")

typing("Please wait...")

gh = usr(usn)

for i in gh:
	lang = ""
	if i["language"] != None:
		lang = i["language"]
	print(i["name"] + " (" + lang + ")")
	
print()

rn = input("Enter repo name: ").replace(" ", "-")

typing("Generating...")

rep = repo(usn, rn)

print(rep["name"])
print(rep["description"])
if rep["language"] != None:
	print(rep["language"])

# print(gh)