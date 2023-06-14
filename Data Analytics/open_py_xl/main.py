from openpyxl import *

class xl:
	def __init__(self, filename: str = ""):
		if filename == "":
			self.filename = "Book2.xlsx"
		else:
			self.filename = filename
		self.xl = load_workbook(self.filename)
	
	def create_s(self, sheet_name: str = ""):
		self.xl_s = self.xl.active
		if not sheet_name == "":
			self.xl_s.title = sheet_name
	
	def set_column(self, cols: list):
		self.xl_s.cell(row = 1, column = 1, value = "ID")
		for a in range(len(cols)):
			self.xl_s.cell(row = 1, column = a + 2, value = cols[a])
	
	def read_data(self, position):
		return self.xl_s[position]
	
	def addData(self, data: list = [[]]):
		for a in range(len(data)):
			self.xl_s.cell(row = a + 2, column = 1, value = a + 1)
			for b in range(len(data[a])):
				self.xl_s.cell(row = a + 2, column = b + 2, value = data[a][b])

	def save_it(self, filename: str = ""):
		if filename == "" or not "." in filename:
			self.xl.save(self.filename)
		else:
			self.xl.save(filename)

# Start Here
if __name__ == "__main__":
	data = xl()
	data.create_s("Sample")
	data.set_column([
		"Name",
		"Description",
		"Gender"
	])
	data.addData([
		[
			"Ryann Kim Sesgundo",
			"A newbie programmer from Quezon Province",
			"Male"
		],
		[
			"Ryann Kim Sesgundo",
			"A newbie programmer from Quezon Province",
			"Male"
		],
	])
	data.save_it("Book 4.xlsx")