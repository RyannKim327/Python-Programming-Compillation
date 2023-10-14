from bs4 import BeautifulSoup as soup
import requests as req

def search():
	a = req.get(f"https://www.billboard.com/charts/year-end/hot-christian-songs/").text
	b = soup(a, "lxml")
	c = b.findAll("li", class_="o-chart-results-list__item")
	d = []
	for e in range(1, len(c)):
		f = c[e].find("h3")
		g = c[e].find("span")
		if(f != None):
			h = f.text.replace("\n", "").replace("\t", "").replace("\r","")
			i = g.text.replace("\n", "").replace("\t", "").replace("\r","")
			j = "Title: " + h + "\nAuthor: " + i
			d.append(j)
	return d

a = search()
for i in range(len(a)):
	print(str(i + 1) + ": " + a[i])