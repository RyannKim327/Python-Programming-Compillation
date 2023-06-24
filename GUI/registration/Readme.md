### GUI with OpenPyXl (Python Programming)
#### MPOP Reverse II
---
<h3 align='center'>Table of contents</h3>

| | |
| --- | --- |
| [Packages](#packs) | [Introduction](#introduction) |
| [Create a workbook](#create-workbook) | [Save](#save)

---
<h3 id="packs">Packages</h3>

**Tkinter**
```Bash
pip install tk
```
or
```Bash
pip install tkinter
```

**OpenPyXL**
```Bash
pip install openpyxl
```

**os**

---
<h3 id="introduction">Introduction</h3>

> In this project, you've must know how to create an excell file, and how to store some data, as well as to get some data from it, you are also expected to learn on how to update and delete.

---
<h3 id="create-workbook">Create a workbook</h3>

> So in this section, you've must learn how to create a workbook. But in this case, I'm using `import os` so that I may know if the excell file is existed or not.
```Python
import openpyxl as xl
import os

filename = "book.xlsx"
sheet_name = "books"

if os.path.exists(filename):
	# Load the file
	wb = xl.load_workbook(filename)
	# Load the sheet
	ws = wb[sheet_name]
else:
	# Create a new Workbook
	wb = xl.Workbook()
	# .active is to create a new sheet if there is none
	ws = wb.active
	# change the name of the sheet
	ws.title = sheet_name
```

> After you create this things, you may now start.

---
<h3 id="save">Save</h3>

> Since you already have the code, to save it as a file, you just need to use `wb.save(filename)` at the last line which looks like this:

```Python
import openpyxl as xl
import os

filename = "book.xlsx"
sheet_name = "books"

if os.path.exists(filename):
	# Load the file
	wb = xl.load_workbook(filename)
	# Load the sheet
	ws = wb[sheet_name]
else:
	# Create a new Workbook
	wb = xl.Workbook()
	# .active is to create a new sheet if there is none
	ws = wb.active
	# change the name of the sheet
	ws.title = sheet_name

wb.save(filename)
```