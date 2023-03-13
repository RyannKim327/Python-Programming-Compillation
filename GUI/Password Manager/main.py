from tkinter import Tk, Entry, Button, mainloop, messagebox, Listbox, Frame, Label, X, BROWSE
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
	datas = getAllData()
	datas[encrypt(key)] = encrypt(value)
	commit(datas)
	print(key, datas.get(encrypt(key)))
	if datas.get(encrypt(key)) == "" or datas.get(encrypt(key)) == None:
		keys = decrypt(list(getAllData().keys())[len(list(getAllData().keys())) - 1])
		listsbox.insert(len(list(getAllData().keys())) - 1, keys)

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

add = Button(base, text="Add Data")
add.config(command=lambda: setData(entry_key.get(), entry_value.get()))
add.pack(fill=X)

global listsbox

listsbox = Listbox()

if len(getAllData().keys()) > 0:
	for i in range(len(getAllData().keys())):
		key = decrypt(list(getAllData().keys())[i])
		listsbox.insert(i, key)


listsbox.pack()
base.mainloop()