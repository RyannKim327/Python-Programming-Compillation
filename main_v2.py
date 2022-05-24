# Imports
from tkinter import Tk, Label, Button, mainloop
from tkinter import messagebox

# Show dialog and text change
def show_up():
	print("sample")
	messagebox.showinfo("Title", "I'm just a noob")
	label.config(text = "Clicked")

# Main function
def main():

	# Setting up window
	window = Tk()
	window.title("My Simple Code")
	window.geometry("300x300")

	# Making label (variable) as global
	# To make it callable from other functions
	global label

	# Setting up label
	label = Label(text="Hello World")
	label.pack()

	# Setting up button
	button = Button(text="Click me")
	# Adding configurations with calling function (action)
	button.config(command=show_up)
	button.pack()

	mainloop()

# Calling main method
main()

'''
This is just my simple code of python (GUI) using Tkinter
Credits to
	TutorialsPoint
	GeeksForGeeks
	Replit
'''
