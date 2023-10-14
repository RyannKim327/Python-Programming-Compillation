from bs4 import BeautifulSoup
import requests

domain = "https://books.goalkicker.com/"

def s():
	a = requests.get(domain).text
	b = BeautifulSoup(a, "lxml")
	c = []
	d = b.find_all("div", class_="bookContainer")
	for i in range(len(d)):
		e = {
			"title": d[i].text,
			"link": d[i].find("a")["href"]
		}
		c.append(e)
	return c

def search(book):
	a = s()
	b = {}
	for i in range(len(a)):
		c = a[i]["title"].lower().replace(" ", "")
		d = book.lower().replace(" ", "")
		if c.startswith(d):
			b = a[i]
			break
	return b

def dl(book):
	a = search(book)
	b = requests.get(domain + a["link"]).text
	c = BeautifulSoup(b, "lxml")
	d = c.find("button", class_="download")["onclick"]
	e = d.replace("location.href=", "").replace("'", "")
	return domain + a["link"] + e

a = input("Enter Programming Language: ")
print(dl(a))