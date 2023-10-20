
class Book:
	def __init__(self, ID, name, author, pub, stocks=0):
		self.ID = ID
		self.name = name
		self.author = author
		self.pub = pub
		self.stocks = stocks
	
	def getBookname(self):
		return self.name


class Librarian:
	def __init__(self, ID, name, books_added):
		self.ID = ID
		self.name = name
		self.books_added = books_added

	def getName(self):
		return self.name

students = []
librarians = []
books = []

book1 = Book(1, "Sample 123", "Kim", "Jiro inc.", 10)

books.append(book1)

for book in books:
	print(book.name)

print("Librarian")

librarian = Librarian(1, "Kim", 10)
librarians.append(librarian)

