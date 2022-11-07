# Python code
import requests as req
import json

def verse(v):
	a = req.get(f"https://getbible.net/json?p={v}&version=tagalog").text
	b = a.replace("(", "").replace(")", "").replace(";", "")
	c = json.loads(b)["book"]
	return c

a = input("Enter Bible Verse: ")
b = verse(a)
c = ""
for d in b:
	c += d["book_name"] + " "
	c += d["chapter_nr"] + "\n"
	e = d["chapter"].keys()
	for f in e:
		c += "[" + str(f) + "] "
		c += d["chapter"][str(f)]["verse"]

print(c)

# Sinearch ko ung kung paano kunin ung lahat ng existing key na meron sa isang object