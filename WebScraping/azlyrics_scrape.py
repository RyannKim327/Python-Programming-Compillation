from bs4 import BeautifulSoup
import requests

def search(song, key):
	title = song.replace(" ", "+")
	url = f"https://search.azlyrics.com/search.php?q={title}&w=songs&p=1&x={key}"
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
k = input("Enter your key: ")
x = search(title, key)

for i in range(len(x)):
	z = x[i]
	a = "[" + str(i + 1) + "]"
	print(a + " Title: " + z["title"] + " - " + z["artist"])

songID = int(input("Enter song ID: "))
y = song(x[songID - 1]["link"])
print(y["title"], "-", y["artist"])
print(y["lyrics"])
