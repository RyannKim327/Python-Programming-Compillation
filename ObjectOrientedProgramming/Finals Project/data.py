import json, os
from tkinter import messagebox
from PyPDF2 import PdfReader

# ----------------- Extracting PDF Document ---------------- #
class PDFExtractor:
	"""This is to get all the text from the pdf file"""

	def __init__(self, filePath: str):
		try:
			reader = PdfReader(filePath)
			self.__texts = "---- 1 ----\n\n"
			self.__results = []
			for i in range(len(reader.pages)):
				self.__texts += reader.pages[i].extract_text()
				if i < len(reader.pages) -1:
					self.__texts += f"\n\n---- {i + 2} ----\n\n"
					self.__results.append(reader.pages[i].extract_text())
		except FileNotFoundError as e:
			self.__texts = ""
			messagebox.showerror("File existence error", "There's no file existed.")
		except Exception as e:
			print(e)
			self.__texts = ""
			messagebox.showerror("File existence error", "This is not a PDF File.")

	def __str__(self):
		return self.__texts

	def __iter__(self):
		return self.__results
# ------------------------------------------------------------------- #

# ---------------------- Setup of Database ---------------------- #
class Database:
	"""This class is used to create a database which is a json file to store data from the application."""
	def __init__(self):
		self._file = "data.json"
		try:
			with open(self._file, "r") as file:
				self._data = json.load(file)
		except Exception as e:
			messagebox.showwarning("Warning", "The database is not existed, so the system automatically generates it.")
			self._data = {
				"data": {}
			}
			with open(self._file, "w") as file:
				file.write(json.dumps(self._data, indent=4))

	def getData(self):
		return self._data

	def deleteData(self, key: str):
		if messagebox.askyesno("Confirmation", "Are you sure you want to remove this document?"):
			self._data.pop(key)
			messagebox.showinfo("Success", "Data Removed Successfully")

	def removeAllData(self):
		if messagebox.askyesno("Confirmation", "All data will never be retribed once you proceed to this action."):
			self._data.clear()

	def saveData(self):
		with open(self._file, "w") as file:
			file.write(json.dumps(self._data, indent=4))
		messagebox.showinfo("Success", "The data was saved.")

class Document(Database):
	def addDocument(self, title: str, author: str, content: str):
		_title = title.upper().strip().replace(" ", "_")
		if self.isExistData(_title):
			self.getData()['data'][_title].append({
				"author": author,
				"content": content
			})
		else:
			self.getData()['data'][_title] = [{
				"author": author,
				"content": content
			}]
		with open(self._file, "w") as file:
			file.write(json.dumps(self._data, indent=4))

	def getDocument(self, title):
		try:
			with open(self._file, "r") as file:
				__data = json.load(self._file)['data']
			return __data[title.strip().upper().replace(" ", "_")]
		except Exception as e:
			return "There is no document existed to the system"

	def isExistData(self, title: str):
		"""Return true if existed"""
		try:
			with open(self._file, "r") as file:
				__data = json.load(self._file)['data']
			return __data.get(title.strip().upper().replace(" ", "_")) != None
		except Exception as e:
			return False
# ------------------------------------------------------------------- #