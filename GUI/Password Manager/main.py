from tkinter import * # Tk, Entry, Button, mainloop, messagebox, Listbox, Frame, Label, X, BROWSE
from tkinter import messagebox
import json
import base64

def encrypt(text: str) -> str:
	return base64.b64encode(text.encode("ascii")).decode("ascii")

def decrypt(text: str) -> str:
	return base64.b64decode(text.encode("ascii")).decode("ascii")

def getAllData() -> dict:
	with open("passwords.json", "r") as f:
		return json.loads(f.read())

def commit(datas: dict):
	with open("passwords.json", "w") as f:
		f.write(json.dumps(datas))

def setData(key: str, value):
	if key == "" or value == "":
		messagebox.showerror("Error", "Keys or Value must not be empty")
	else:
		datas = getAllData()
		if datas.get(encrypt(key)) == "" or datas.get(encrypt(key)) == None:
			listsbox.insert(len(list(getAllData().keys())), key)
		datas[encrypt(key)] = encrypt(value)
		commit(datas)

def check():
	for i in listsbox.curselection():
		title = listsbox.get(i)
		datas = getAllData()
		messagebox.showinfo(title, decrypt(datas[encrypt(title)]))

base = Tk()
base.title("Password Manager")
base.geometry("300x300")
base.resizable(False, False)

frame_key = Frame(base)

label_key = Label(frame_key, text="Key: ")
label_key.pack(side='left')

entry_key = Entry(frame_key)
entry_key.pack(fill=X)

frame_key.pack(fill=X)

frame_value = Frame(base)

label_value = Label(frame_value, text="Value: ")
label_value.pack(side='left')

entry_value = Entry(frame_value)
entry_value.pack(fill=X)

frame_value.pack(fill=X)

frame_button = Frame(base)

add = Button(frame_button, text="Add Data")
add.config(command=lambda: setData(entry_key.get(), entry_value.get()), width=20)
add.pack(side=LEFT)

mod = Button(frame_button, text="Modify Data")
mod.pack(side=RIGHT)

frame_button.pack(fill=X)

chk = Button(base, text="Check data", command=check)
chk.config(width=20)
chk.pack(fill=X)

global listsbox

listsbox = Listbox()

if len(getAllData().keys()) > 0:
	for i in range(len(getAllData().keys())):
		key = decrypt(list(getAllData().keys())[i])
		listsbox.insert(i, key)

listsbox.pack(fill=BOTH)

base.mainloop()