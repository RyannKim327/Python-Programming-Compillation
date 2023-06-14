from openpyxl import *

# Creating a workbook
wb = Workbook()

# Create a sheet
ws = wb.active

# Load Workbook
# wb = load_workbook('Book1.xlsx')

# Create Columns
a = [
	"ID",
	"Name",
	"Description"
]
for b in range(len(a)):
	ws.cell(row=1, column=(b + 1), value=a[b])

ws.cell(row=2, column=1, value=1)
ws.cell(row=2, column=2, value="Ryann Kim Sesgndo")
ws.cell(row=2, column=3, value="Newbie")

wb.save("Book2.xlsx")