
class Book:
	def __init__(self, ID, name, author, pub, stocks=0):
		self.ID = ID
		self.name = name
		self.author = author
		self.pub = pub
		self.stocks = stocks
	
	def getBookname(self):
		return self.name

students = []
librarian = []
books = []

book1 = Book(1, "Sample", "Kim", "Jiro inc.", 10)

books.append(book1)

for book in books:
	print(book.getBookname())