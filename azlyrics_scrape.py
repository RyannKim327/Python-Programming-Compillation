from bs4 import BeautifulSoup
import requests

def search(song):
	title = song.replace(" ", "+")
	url = f"https://search.azlyrics.com/search.php?q={title}&w=songs&p=1&x=807b5ad26a33a2db86cf868f8894c9505197d9565f06b2d584ff5ebe602422ce"
	r = requests.get(url).text
	b = BeautifulSoup(r, "lxml")
	m = b.find("div", class_="main-page")
	s = m.find("table", class_="table-condensed")
	y = s.find_all("td", class_="visitedlyr")
	a = []
	for i in y:
		b = i.find_all("b")
		t = b[0].text
		ar = b[1].text
		l = i.find("a")["href"]
		d = {
			"title": t,
			"artist": ar,
			"link": l
		}
		a.append(d)
	return a

def song(url):
	r = requests.get(url).text
	b = BeautifulSoup(r, "lxml")
	tc = b.find("div", class_="col-xs-12 col-lg-8 text-center")
	l = tc.find_all("div")[5].text
	_t = b.find_all("div", class_="div-share")[1]
	t = _t.find("h1").text
	a = b.find("div", class_="lyricsh").find("b").text
	d = {
		"title": t,
		"artist": a,
		"lyrics": l
	}
	return d

title = input("Search a title: ")
x = search(title)

for i in range(len(x)):
	z = x[i]
	a = "[" + str(i + 1) + "]"
	print(a + " Title: " + z["title"] + " - " + z["artist"])

songID = int(input("Enter song ID: "))
y = song(x[songID - 1]["link"])
print(y["title"], "-", y["artist"])
print(y["lyrics"])