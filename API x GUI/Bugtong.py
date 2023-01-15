from tkinter import *
import requests
import json

def getResult():
	api = requests.get("https://api-pinoy-bugtong.vercel.app").text
	return json.loads(api)

def check():
	if entry.get() in res['s']:
		label.config(text = "Nice")
	else:
		label.config(text = f"No the correct answer is {res['s']}")
	
	button.config(text = "Click again to continue", command = restart)

def restart():

	global res

	res = getResult()

	label.config(text = res['b'])
	entry.delete(0, END)
	button.config(text = "Verify Answer", command = check)

def start():

	global base
	global label
	global entry
	global button

	base = Tk()
	base.geometry("500x500")
	base.title("Pinoy Bugtong")

	label = Label()
	label.pack()

	entry = Entry()
	entry.pack()

	button = Button()
	button.pack()
	
	restart()

	mainloop()

start()