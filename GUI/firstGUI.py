import tkinter as tk
from tkinter import messagebox

def show_up():
	print("sample")
	messagebox.showinfo("Title", "I'm just a noob")

def main():

	window = tk.Tk()
	window.title("My Simple Code")
	window.geometry("300x300")

	label = tk.Label(text="Hello World")
	label.pack()

	button = tk.Button(text="Click me", command=show_up)
	button.pack()

	tk.mainloop()

main()
