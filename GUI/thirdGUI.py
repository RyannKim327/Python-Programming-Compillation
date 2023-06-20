'''
You may use VSCode or Pydroid 3. Pwede ding Replit
to install tkinter, sa pydroid, punta kayo sa nav menu then click pip tas input nyo sa library name is tkinter

to install sa replit or vscode, punta kayo sa terminal or console, or shell, then execute this code
pip install tkinter
'''

# imports
from tkinter import *

# use as alert
from tkinter import messagebox

# Function once the button triggered
def change():
	val = _input.get()
	text.config(text=val)
	messagebox.showinfo("Title", "Text Here")

# Base of Tkinter UI
tk = Tk()
tk.title("Simple TKinter")
tk.geometry("300x300")

# Text Area
text = Label(text="Hello world")
text.config(text="MPOP Reverse II")
text.pack()

# Input Box
_input = Entry()
_input.pack()

# Button
click = Button(text="Change the text", command=change)
click.pack()

# To show the UI
tk.mainloop()