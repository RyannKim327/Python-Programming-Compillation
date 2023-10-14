### GUI with OpenPyXL (Python Programming)
#### MPOP Reverse II

---
<h3 align='center'>Table of contents</h3>

| | |
| --- | --- |
| [Packages](#packs) | [Introduction](#introduction) |
| [Create a workbook](#create-workbook) | [Save](#save) |
| [Add Column Names](#add-columns) | [Add some data](#add-data) |
| [Read data](#read-data) |

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

# Check if the file exists
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

# Check if the file exists
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

# Save as file
wb.save(filename)
```

> If the file isn't existed, it will automatically generate the file there in same directory of your python file.

---
<h3 id="add-columns">Add Column names</h3>

> So since we use excell as database, we will going to add some columns inside of your else, if you follow the first step of this tutorial, and this is my way to easily recognized for the data where I need to use. At this point, we need first to create an array or list, lets named it `column`

```Python
column = [
	"ID",
	"name",
	"age",
	"address"
]

# Then, we will going to create a loop.

for i in range(len(column)):
	# let us add some data by help of cell function
	# ws is the worksheet where we're working on
	ws.cell(row = 1, cell = (i + 1), value = column[i])

```

> Excell is not an indexing type, where it is starts in zero. Excell always starts with `1` as primary cell and row. So the final code may look like this

```Python
import openpyxl as xl
import os

filename = "book.xlsx"
sheet_name = "books"

# Check if the file exists
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


	# Add some column name
	column = [
		"ID",
		"name",
		"age",
		"address"
	]

	# Then, we will going to create a loop.

	for i in range(len(column)):
		# let us add some data by help of cell function
		# ws is the worksheet where we're working on
		ws.cell(row = 1, cell = (i + 1), value = column[i])

# Save as file
wb.save(filename)
```

> It is actually included inside of your else, **WHY?** Because, we alrady have some data inside of the excell file if we done it before, so that we may not have some troubles regarding in adding of some column inside of it.

---
<h3 id="add-data">Add some data</h3>

> In this section, we will going to use the `list method`, instead of using `tuple`. So just like the past tutorial on how to add some column names, it almost the same thing:

```Python
# First is you need to have the lists of data
data = [
	"book_001", # as ID
	"Harry Potter", # as name
	"22", # as age of the book
	"National Bookstore" # as address or location
]

# next is we need to loop it
rows = ws.max_row + 1
for i in range(len(data)):
	ws.cell(row = rows, column = i + 1, value = data[i])

```

> So the reason why we need to get the last row, is for us to identify where we will going to put the data. So the final code may look like this:


```Python
import openpyxl as xl
import os

filename = "book.xlsx"
sheet_name = "books"

# Check if the file exists
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

	# Add some column name
	column = [
		"ID",
		"name",
		"age",
		"address"
	]

	# Then, we will going to create a loop.

	for i in range(len(column)):
		# let us add some data by help of cell function
		# ws is the worksheet where we're working on
		ws.cell(row = 1, cell = (i + 1), value = column[i])

# First is you need to have the lists of data
data = [
	"book_001", # as ID
	"Harry Potter", # as name
	"22", # as age of the book
	"National Bookstore" # as address or location
]

# next is we need to loop it
rows = ws.max_row + 1
for i in range(len(data)):
	ws.cell(row = rows, column = i + 1, value = data[i])


# Save as file
wb.save(filename)
```

---
<h3 id="read-data">Read data</h3>

> In this section, you may learn how to get a data from your excell file or bunch of data from your excell file.

```Python
# First is you need to create an empty lists
data = []

# Then we will going to append it, so this one is to print all the data row by row

for i in ws.iter_rows(values_only=True):
	temp_data = []
	for j in i:
		temp_data.append(i)
	data.append(temp_data)

# The result of this was a 2d array or:

# data = [
# 	["ID", "name", "age", "address"],
# 	["ID", "name", "age", "address"],
# 	["ID", "name", "age", "address"],
# 	["ID", "name", "age", "address"]
# ]

# Just ignore the # in the output, just only a representation. the next one is to get column by column

for i in ws.iter_cols(values_only=True):
	temp_data = []
	for j in i:
		temp_data.append(i)
	data.append(temp_data)

# The result of this was a 2d array or:

# data = [
# 	["ID", "ID", "ID", "ID"],
# 	["name", "name", "name", "name"],
# 	["age", "age", "age", "age"],
# 	["address", "address", "address", "address"]
# ]

```

> So, there are two final result:

**[Row]**

```Python
import openpyxl as xl
import os

filename = "book.xlsx"
sheet_name = "books"

# Check if the file exists
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

	# Add some column name
	column = [
		"ID",
		"name",
		"age",
		"address"
	]

	# Then, we will going to create a loop.

	for i in range(len(column)):
		# let us add some data by help of cell function
		# ws is the worksheet where we're working on
		ws.cell(row = 1, cell = (i + 1), value = column[i])

# First is you need to have the lists of data
data = [
	"book_001", # as ID
	"Harry Potter", # as name
	"22", # as age of the book
	"National Bookstore" # as address or location
]

# next is we need to loop it
rows = ws.max_row + 1
for i in range(len(data)):
	ws.cell(row = rows, column = i + 1, value = data[i])

# Get the data by rows
# First is you need to create an empty lists
data = []

# Then we will going to append it, so this one is to print all the data row by row

for i in ws.iter_rows(values_only=True):
	temp_data = []
	for j in i:
		temp_data.append(i)
	data.append(temp_data)

# Save as file
wb.save(filename)
```

**[Columns]**

```Python
import openpyxl as xl
import os

filename = "book.xlsx"
sheet_name = "books"

# Check if the file exists
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

	# Add some column name
	column = [
		"ID",
		"name",
		"age",
		"address"
	]

	# Then, we will going to create a loop.

	for i in range(len(column)):
		# let us add some data by help of cell function
		# ws is the worksheet where we're working on
		ws.cell(row = 1, cell = (i + 1), value = column[i])

# First is you need to have the lists of data
data = [
	"book_001", # as ID
	"Harry Potter", # as name
	"22", # as age of the book
	"National Bookstore" # as address or location
]

# next is we need to loop it
rows = ws.max_row + 1
for i in range(len(data)):
	ws.cell(row = rows, column = i + 1, value = data[i])

# Get the data by columns
# First is you need to create an empty lists
data = []

# Then we will going to append it, so this one is to print all the data column by column

for i in ws.iter_cols(values_only=True):
	temp_data = []
	for j in i:
		temp_data.append(i)
	data.append(temp_data)

# Save as file
wb.save(filename)
```
---