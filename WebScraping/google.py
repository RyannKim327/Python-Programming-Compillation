from bs4 import BeautifulSoup as soup
import requests as req

def getData(query):
	a = req.get(f"https://www.google.com/search?q={query}").text
	return a

def scrape(query):
	data = getData(query)
	bs = soup(data, "lxml")
	data2 = bs.find("div", class_="PZPZlf")
	print(data2)

scrape("broken vessels lyrics")