from bs4 import BeautifulSoup as soup
from tkinter import Tk, Label, Entry, Button, Frame, mainloop
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
				"text": title,
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

def go():
	base.title("Scrapping...")
	a = word(e.get())[0]
	if(a["result"] == "200"):
		b = "Text: " + a["text"] + "\n"
		b += "Parts of Speech: " + a["parts_of_speech"] + "\n"
		b += "Syllable: " + a["syllable"] + "\n"
		b += "Definitions: " + a["def"] + "\n"
		
		l.config(text = b)
	else:
		l.config(text = "Error")
	base.title("Webscrape with GUI Merriam Webster")

def main():
	global l
	global e
	global base
	
	base = Tk()
	base.title("Webscrape with GUI Merriam Webster")
	base.geometry("700x900")
	
	f = Frame(base)
	g = Frame(f)
	
	e = Entry(g, width = "10")
	e.pack()
	
	b = Button(g, text = "Search")
	b.config(command = go)
	b.pack()
	
	g.pack()
	
	l = Label(f, wrap = "500")
	l.pack()
	
	f.pack()
	mainloop()

main()