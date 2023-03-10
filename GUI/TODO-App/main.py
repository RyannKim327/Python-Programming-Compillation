import json
from tkinter import *

class dataset:
	def __init__(self):
		self._josn = json.loads(open("data.json", "r").read())
	
	def getData(self) ->  dict:
		return self._josn
	

datas = dataset()
todos = datas.getData()

def done(key: int):
	todos[key]['done'] = not todos[key]['done']
	f = open("data.json", "w")
	f.write(json.dumps(todos))
	print(todos)

base = Tk()
base.title("TODO App")
base.geometry("300x300")


checker = []

for todo in range(len(todos)):
	i = todos[todo]
	v = BooleanVar(name=i["info"])
	checker.append(Checkbutton(base, text=i['data'], variable=v, onvalue=True, offvalue=False))
	
for i in range(len(checker)):
	if bool(todos[i]['done']):
		checker[i].select()
		checker[i].pack()
		checker[i].config(command=lambda: done(todos[i]['n']))
	else:
		checker[i].deselect()
		checker[i].pack()
		checker[i].config(command=lambda: done(todos[i]['n']))

base.mainloop()