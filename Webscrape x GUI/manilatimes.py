from tkinter import Tk, Text, Entry, Button, Frame, Scrollbar, mainloop, END
from bs4 import BeautifulSoup as soup
import requests as req

def lists():
	data = req.get("https://www.manilatimes.net/news").text
	html = soup(data, "lxml")
	body = html.findAll("div", class_="item-row")
	a = []
	for i in body:
		url = i.find("a", class_="item-info-abs-href")
		if url != None:
			b = {
				"link": url["href"],
				"title": url["title"]
			}
			a.append(b)
	return a

def article(link):
	data = req.get(link).text
	html = soup(data, "lxml")
	title = html.find("h1", class_="article-title").text.replace("\n", "").replace("  ", "")
	info_container = html.find("div", class_="article-info-container")
	author = info_container.find("a", class_="article-author-name")
	if author != None:
		author = author.text.replace("\n", "").replace("  ", "")
	else:
		author = ""
	date = info_container.find("div", class_="article-publish-time")
	if date != None:
		date = date.text.replace("\n", "").replace("  ", "")
	else:
		date = ""
	caption = html.find("div", class_="article-image-caption")
	if caption != None:
		caption = caption.text
	else:
		caption = ""
	article_body = html.find("div", class_="article-body-content")
	p = article_body.findAll("p")
	a = []
	for i in p:
		if i.text != " ":
			a.append(i.text)
	b = {
		"title": title,
		"author": author,
		"time": date,
		"imgCaption": caption,
		"article": a
	}
	return b

def art():
	lab.insert(END, "Please wait...\n\n\n")
	base.title("Scraping...")
	
	try:
		a = int(ent.get())
		b = lists()
		c = article(b[a - 1]["link"])
		d = c["title"] + "\n"
		d += c["author"] + " - " + c["time"] + "\n"
		d += c["imgCaption"] + "\n"
		for i in c["article"]:
			d += i + "\n"
		lab.insert(END, d)
	except:
		lab.insert(END, "Error")
	base.title("Webscraped with GUI")

def main() :
	global base
	
	base = Tk()
	base.title("Webscraped with GUI")
	base.geometry("700x900")
	
	global lab
	global ent
	
	f = Frame(base)
	s = Scrollbar(f, bd = "0", orient = "vertical")
	
	ent = Entry(f)
	ent.pack()
	
	but = Button(f, text = "Go")
	but.config(command = art)
	but.pack()
	
	lab = Text(s)
	# lab.config(font = ("TimesNewRoman, 12"))
	lab.pack()
	
	a = lists()
	b = ""
	for c in range(len(a)):
		b += str(c + 1) + ": " + a[c]["title"] + "\n"
	
	lab.insert(END, b)
	
	s.pack(fill = "y")
	f.pack()
	
	mainloop()

main()