import json, os
from tkinter import messagebox
from PyPDF2 import PdfReader



# ----------------- Extracting PDF Document ---------------- #
class PDFExtractor:
	def __init__(self, filePath: str):
		"""This is to get all the text from the pdf file"""

		if os.path.exists(filePath):
			reader = PdfReader(filePath)
			self.__texts = "---- 1 ----\n\n"
			for i in range(len(reader.pages)):
				self.__texts += reader.pages[i].extract_text()
				if i < len(reader.pages) -1:
					self.__texts += f"\n\n---- {i + 2} ----\n\n"

		else:
			self.__texts = ""
			messagebox.showerror("File existence error", "There's no file existed.")

	def __str__(self):
		return self.__texts
# ------------------------------------------------------------------- #

# ---------------------- Setup of Database ---------------------- #
class Database:
	def __init__(self):
		"""This class is used to create a database which is a json file to store data from the application."""
		self.__file = "data.json"

	def getData(self):
		try:
			with open(self.__file, "r") as file:
				self.__data = json.load(file)
		except Exception as e:
			messagebox.showwarning("Warning", "The database is not existed, so the system automatically generates it.")
			self.__data = {
				"data": []
			}
			with open(self.__file, "w") as file:
				file.write(json.dumps(self.__data, indent=4))
		return self.__data

	def deleteData(self, key: str):
		if messagebox.askyesno("Confirmation", "Are you sure you want to remove this document?"):
			self.__data.pop(key)
			messagebox.showinfo("Success", "Data Removed Successfully")

	def removeAllData(self):
		if messagebox.askyesno("Confirmation", "All data will never be retribed once you proceed to this action."):
			self.__data.clear()

	def saveData(self):
		with open(self.__file, "w") as file:
			file.write(json.dumps(self.__data, indent=4))
		messagebox.showinfo("Success", "The data was saved.")

class Document(Database):
	def checkDocument(self, title: str, author: str):
		return self.__data[f"{title.lower()}_{author.lower()}"]

	def addDocument(self, title: str, author: str, content: str):
		self.__data[f"{title.lower()}_{author.lower()}"] = {
			"title": title.capitalize(),
			"author": author.capitalize(),
			"content": content
		}
		with open(self.__file, "w") as file:
			file.write(json.dumps(self.__data, indent=4))
# ------------------------------------------------------------------- #
