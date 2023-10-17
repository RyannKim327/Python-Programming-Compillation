import time, getpass

def loading(msg="Please wait for a moment", timer=.25, delay=1.5):
	a = ""
	b = 0
	c = "\\|/-"
	d = 0
	delay *= 100
	while True:
		print(f"{a} {c[d]}", end="\r")
		d += 1
		time.sleep(timer)
		if d >= len(c):
			d = 0
		
		if b < len(msg):
			a += msg[b]
			b += 1
		
		delay -= 1

		if delay <= 0:
			break

	print(end="\r")

def typing(text, timer=0.05):
	for i in text:
		print(i, end="", flush=True)
		time.sleep(timer)
	print()

def insert(text, password=False, timer=0.05):
	for i in text:
		print(i, end="", flush=True)
		time.sleep(timer)
	if text.endswith(":"):
		text += " "
	if not text.endswith(": "):
		text += ": "
	if password:
		return getpass.getpass("")
	return input()

def insertlists(lists: list, prompt="Enter your choice: ", timer=0.1):
	for i in range(len(lists)):
		print(f"[{i + 1}] {lists[i]}")
		time.sleep(timer)
	
	if prompt.endswith(":") or prompt.endswith("?"):
		prompt += " "
	if not prompt.endswith(": ") and not prompt.endswith("? "):
		prompt += ": "
	return insert(prompt)

class Student:
	def __init__(self, student: dict):
		self.__id__ = student['ID']
		self.__student__ = student['studentName']
	
	def getStudentName(self):
		return self.__student__

	def getStudentID(self):
		print(self.__id__)

class Librarian:
	def __init__(self, librarian: dict):
		self.__id__ = librarian['ID']
		self.__name__ = librarian['name']
		self.__password__ = librarian['password']

	def getName(self):
		return self.__name__
	
	def getPassword(self):
		return self.__password__

class Books:
	def __init__(self, book: dict):
		self.__id__ = book['ID']
		self.__name__ = book['title']
		self.__author__ = book['author']
		self.__publisher__ = book['publisher']
		self.__date__ = book['date']
		self.__stocks__ = book['stocks']
	
	def  getBookName(self):
		return self.__name__
	
	def canBorrow(self):
		return self.__stocks__ > 0
	
	def doBorrow(self, studentName):
		if self.canBorrow:
			self.__stocks__ -= 1
			print(f"The book was borrowed by {studentName}")
		else:
			print(f"There's no books for now. Please wait until they return the books to us.")

	def doReturn(self, studentName):
		self.__stocks__ += 1
		print(f"The book was returned by {studentName}")

	def getStocks(self):
		return self.__stocks__