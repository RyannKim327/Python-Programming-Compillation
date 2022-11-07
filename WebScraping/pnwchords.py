from bs4 import BeautifulSoup as soup
import requests as req

link = "https://pnwchords.com/"

def search(song):
	title = song.replace(" ", "+")
	a = req.get(link + "?s=" + title).text
	b = soup(a, "lxml")
	c = b.findAll("h2", class_="post-title")
	d = []
	for e in range(len(c)):
		f = c[e].find("a")
		g = f["href"]
		h = {
			"url": g,
			"title": f.text
		}
		d.append(h)
	return d

def chords(url):
	a = req.get(url).text
	b = soup(a, "lxml")
	c = b.find("div", class_="tabcontent")
	d = c.find("pre").text
	return d

a = input("Enter a worship song title: ")
b = search(a)
c = chords(b[0]["url"])
print(c)