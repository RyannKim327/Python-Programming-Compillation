from bs4 import BeautifulSoup as BeautifulCanton
import requests as req

def getLanguages():
	data = req.get("https://wikipedia.com").text
	html = BeautifulCanton(data, "lxml")
	body = html.find("select", id="searchLanguage")
	lang = body.findAll("option")
	res = []
	for i in lang:
		res.append(i.text + " -> " + i["value"])
	return res

def open(search, lang):
	if lang == "":
		lang = "en"
	data = req.get(f"https://www.wikipedia.org/search-redirect.php?search={search}&language={lang}").text
	html = BeautifulCanton(data, "lxml")
	body = html.findAll("p")
	img = "https:" + html.find("img", class_="thumbimage")["src"]
	res = []
	for i in range(1, len(body)):
		res.append(body[i].text)
	output = {
		"results": res,
		"image": img
	}
	return output

lang = getLanguages()
print("Lists of languages:", lang)

print()
search = input("Search on wiki: ")
keyLang = input("Two letter key language: ")

res = open(search, keyLang)
for i in res["results"]:
	print(i)

print("Image:", res["image"])