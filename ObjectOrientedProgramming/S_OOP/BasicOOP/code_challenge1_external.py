class Student:
	def __init__(self, student: dict):
		self._id_ = student['ID']
		self._student_ = student['studentName']


class Librarian:
	def __init__(self, librarian: dict):
		self._id_ = librarian['ID']
		self._name_ = librarian['name']
		self._password_ = librarian['password']
		pass

class Books:
	def __init__(self, book: dict):
		self._id_ = book['ID']
		self._name_ = book['title']
		self._author_ = book['author']
		pass