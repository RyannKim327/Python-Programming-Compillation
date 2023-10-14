from bs4 import BeautifulSoup as soup
import requests as req

def lists():
	data = req.get("https://www.manilatimes.net/news").text
	html = soup(data, "lxml")
	body = html.findAll("div", class_="item-row")
	a = []
	for i in body:
		url = i.find("a", class_="item-info-abs-href")
		if url != None:
			b = {
				"link": url["href"],
				"title": url["title"]
			}
			a.append(b)
	return a

def article(link):
	data = req.get(link).text
	html = soup(data, "lxml")
	title = html.find("h1", class_="article-title").text.replace("\n", "").replace("  ", "")
	info_container = html.find("div", class_="article-info-container")
	author = info_container.find("a", class_="article-author-name")
	if author != None:
		author = author.text.replace("\n", "").replace("  ", "")
	else:
		author = ""
	date = info_container.find("div", class_="article-publish-time")
	if date != None:
		date = date.text.replace("\n", "").replace("  ", "")
	else:
		date = ""
	caption = html.find("div", class_="article-image-caption")
	if caption != None:
		caption = caption.text
	else:
		caption = ""
	article_body = html.find("div", class_="article-body-content")
	p = article_body.findAll("p")
	a = []
	for i in p:
		if i.text != " ":
			a.append(i.text)
	b = {
		"title": title,
		"author": author,
		"time": date,
		"imgCaption": caption,
		"article": a
	}
	return b

a = lists()
for i in range(len(a)):
	print(str(i + 1) +  ": " + a[i]["title"])

print()
b = int(input("Enter the number of acticle: "))

print()

c = article(a[b - 1]["link"])
print(c["title"])
print(c["author"], "-", c["time"])
print(c["imgCaption"])
for i in c["article"]:
	print(i)
