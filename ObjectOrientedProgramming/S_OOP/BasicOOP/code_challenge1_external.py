class Student:
	def __init__(self, student: dict):
		self._id_ = student['ID']
		self._student_ = student['studentName']
	
	def getStudentName(self):
		print(self._student_)

	def getStudentID(self):
		print(self._id_)

class Librarian:
	def __init__(self, librarian: dict):
		self._id_ = librarian['ID']
		self._name_ = librarian['name']
		self._password_ = librarian['password']

	def getName(self):
		return self._name_
	
	def getPassword(self):
		return sl

class Books:
	def __init__(self, book: dict):
		self._id_ = book['ID']
		self._name_ = book['title']
		self._author_ = book['author']
		self._publisher_ = book['publisher']
		self._date_ = book['date']
	
	def  getBookName(self):
		return self._name_