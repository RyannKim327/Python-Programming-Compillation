from bs4 import BeautifulSoup as soup
import requests as req

def getData(query):
	a = req.get(f"https://www.google.com/search?q={query}").text
	return a

def scrape(query):
	data = getData(query)
	bs = soup(data, "html.parser")
	