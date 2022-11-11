from bs4 import BeautifulSoup as soup
import requests as req

def lists():
	data = req.get("https://www.manilatimes.net").text
	html = soup(data, "lxml")
	body = html.findAll("div", class_="item-row")
	a = []
	for i in body:
		url = i.find("a")
		if url["href"] != None:
			b = {
				"link": url["href"],
				"title": url.text
			}
			a.append(i)
	return b

def article(link):
	data = req.get(link).text
	html = soup(data, "lxml")
	title = html.find("h1", class_="article-title").text.replace("\n", "").replace("  ", "")
	info_container = html.find("div", class_="article-info-container")
	author = info_container.find("a", class_="article-author-name").text.replace("\n", "").replace("  ", "")
	date = info_container.find("div", class_="article-publish-time").text.replace("\n", "").replace("  ", "")
	caption = html.find("div", class_="article-image-caption").text
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

a = "https://www.manilatimes.net/2022/11/11/news/marcos-accepts-xis-invitation-to-visit-china-in-january/1865947"
b = "https://www.manilatimes.net/2022/11/11/latest-stories/meralco-registers-1st-back-to-back-wins-in-tournament/1865988"

c = article(a)
#print(c["title"])
#print(c["author"], "-", c["time"])
#print(c["imgCaption"])
#for i in c["article"]:
#	print(i)
print(lists())