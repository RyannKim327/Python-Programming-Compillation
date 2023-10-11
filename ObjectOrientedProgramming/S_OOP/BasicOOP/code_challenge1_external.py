class Student:
	def __init__(self, student: dict):
		self.__id__ = student['ID']
		self.__student__ = student['studentName']
	
	def getStudentName(self):
		print(self.__student__)

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
		self._author_ = book['author']
		self._publisher_ = book['publisher']
		self._date_ = book['date']
	
	def  getBookName(self):
		return self.__name__