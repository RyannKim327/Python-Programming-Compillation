# import
from tkinter import Label, Button, Entry, Tk, mainloop, messagebox

appName = "My Sample Program"
pixels = "300x300"

def show_dialog():
	
	messagebox.showinfo(appName, "Active window")
	# checking if entry has value
	if entry.get() != "":
		label.config(text = entry.get())
	else:
		label.config(text = "No value")

def main():
	
	# Setting up window
	window = Tk()
	window.title(appName)
	window.geometry(pixels)
	
	# Making label and entry accessible from other functions
	global label
	global entry
	
	# variable declarations
	label = Label()
	label.config(text = "Hello World")
	label.pack()

	entry = Entry()
	entry.config(width = 40)
	entry.focus_set()
	entry.pack()
	
	button = Button()
	button.config(text = "Click me")
	button.config(command = show_dialog)
	button.pack()
	
	mainloop()
	
# Calling main function
main()

'''
This is just a simple code of Python GUI using TKinter
Credits to
- GeeksForGeeks
- TutorialsPoint
- Replit
'''
