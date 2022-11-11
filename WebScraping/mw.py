#pylint:disable=W0702
from bs4 import BeautifulSoup as soup
import requests as req

def word(w):
	search = w.split(" ")[0]
	data = req.get(f"https://merriam-webster.com/dictionary/{search}").text
	html = soup(data, "lxml")
	body_ = html.find("div", class_="entry-header")
	try:
		title = body_.find("h1", class_="hword").text
		body = html.findAll("div", class_="left-content")
		result = []
		for i in range(len(body)):
			num = body[i].find("span", class_="entry-numbers-badge")
			if num != None:
				num = num.text
			else:
				num = "null"
			speech = body[i].find("h2", class_="parts-of-speech")
			if speech != None:
				speech = speech.text
			else:
				speech = "null"
			syll = body[i].find("span", class_="prons-entries-list-inline")
			if syll != None:
				syll = syll.find("a").text
			else:
				syll = "null"
			definitions = body[i].find("div", class_="vg")
			if definitions != None:
				definitions = definitions.text.replace("\n\n", "")
			else:
				definitions = "null"
			json = {
				"result": "200",
				"title": title,
				"count": num,
				"parts_of_speech": speech,
				"syllable": syll,
				"def": definitions
			}
			result.append(json)
	except:
		result = [{
			"result": "404"
		}]
	return result

a = input("Enter your word: ")
b = word(a)
print(b)