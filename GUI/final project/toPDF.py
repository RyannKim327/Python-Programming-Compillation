from openpyxl import load_workbook
from xtopdf import PDFWriter

def toPDF(excellFile: str, sheetname: str = "",  pdfFile: str = ""):
	result = {
		"done": True,
		"msg": []
	}
	error = []
	if not excellFile.endswith(".xlsx"):
		result['done'] =  False
		error.append("excell file name")
	if not pdfFile.endswith(".pdf"):
		result['done'] = False
		error.append("pdf file name")
	
	result['mgs'] = error
	if result['done']:
		book = load_workbook(excellFile)
		if sheetname == "":
			sheet = book.active
		else:
			sheet = book[sheetname]

		pdf = PDFWriter(pdfFile)
		pdf.setFont("Helvetica", 10)

		for r in sheet.iter_rows(values_only=True):
			r_t = "     ".join(str(cell) for cell in r)
			pdf.writeLine(r_t)
		
		pdf.savePage()
		pdf.close()
		result['msg'] = "Success"
	return result