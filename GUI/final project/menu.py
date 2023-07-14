from tkinter import messagebox, Menu

def getMenu():
	data = []
	with open("ReadMe.md", "r") as file:
		for i in file.read().split("---"):
			data.append(i)
	return data

def showInfo(title):
	x = menus[title]
	messagebox.showinfo(title, f"   {x}")

def menuSetup(root):
	global menus
	baseColor = "#575D5E"
	txtColor = "#ffffff"
	menu = Menu(root, tearoff=False, background=baseColor, foreground=txtColor)
	about = Menu(menu, tearoff=False, background=baseColor, foreground=txtColor)
	menus = {}
	for sets in getMenu():
		set = sets.replace("\n\n", "").split("\n")
		title = ""
		content = ""
		for i in set:
			if i.startswith("### "):
				title = i.replace("### ", "")
			if i.startswith("> "):
				content = i.replace("> ", "")
			if title != "":
				menus[title] = content

	x = list(menus.keys())

	about.add_command(label=x[0], command=lambda: showInfo(x[0]))
	about.add_command(label=x[1], command=lambda: showInfo(x[1]))
	about.add_command(label=x[2], command=lambda: showInfo(x[2]))
	menu.add_cascade(label="Documentation", menu=about)
	root.config(menu=menu)
	return menu