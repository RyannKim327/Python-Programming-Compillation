import os
from openpyxl import load_workbook
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def toPDF(excelFile: str, sheetname: str = "",  pdfFile: str = ""):
	result = {
		"done": True,
		"msg": []
	}
	error = []
	if not excelFile.endswith(".xlsx"):
		result['done'] =  False
		error.append("excell file name")
	if not pdfFile.endswith(".pdf"):
		result['done'] = False
		error.append("pdf file name")
	
	result['mgs'] = error
	if result['done']:
		excel_path = os.path.abspath(excelFile)
		pdf_path = os.path.abspath(pdfFile)

		book = load_workbook(excel_path)
		if sheetname == "":
			sheet = book.active
		else:
			sheet = book[sheetname]
		
		mr = sheet.max_row
		mc = sheet.max_column
		
		can = canvas.Canvas(pdf_path, pagesize=landscape(letter))

		tm = 3 * inch
		lm = 0.75 * inch
		bm = 0.75 * inch
		rm = 0.75 * inch

		cell_width = (11 * inch - lm - rm) / mc 
		cell_height = (8.5 * inch - tm - bm) / mr 

		for row in range(1, mr + 1):
			for col in range(1, mc + 1):
				cell  = sheet.cell(row=row, column=col)
				txt = str(cell.value)

				if col == 4:
					col += 1
				x = lm + (col - 1) * cell_width
				y = 11 * inch - (tm + row * cell_height)
				if col != 3:
					can.drawString(x, y, txt)
		
		can.save()

		result['msg'] = "Success"
	return result