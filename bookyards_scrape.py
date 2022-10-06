from bs4 import BeautifulSoup
import requests

domain = "https://www.bookyards.com/mobile/"

def search(book):
	a = requests.get(f"{domain}authors.php?r={book}&t=book").text
	b = BeautifulSoup(a, "lxml")
	c = b.find_all("a")
	d = []
	for i in range(len(c)):
		if "confirm_book_download" in c[i]["href"]:
			e = c[i]
			f = {
				"title": e.text,
				"link": domain + e["href"]
			}
			d.append(f)
	return d

a = input("Search a book: ")
print(search(a))