# Coded by Ryann Kim Sesgudo
# BSIT 1A (Cluster 2)
# Professor: Mr. Leonard Andrew Mesiera

user = input("Please enter your name: ")

while user == "":
	user = input("Please enter your name: ")

menu = [
	"Printing in Python",
	"Variable Definition",
	"Operators in Python",
	"Conditional in Python",
	"Loop in Python",
	"Functions in Python",
	"Arrays in Python",
	"Dictionary in Python",
	"Exit"
]

def cont():
	print()
	input("Press enter to continue...")
	print("\r")

def close(list):
	print()
	lists = ""
	for i in range(len(list)):
		lists += "[" + str (i + 1) + "]" + " " + list[i][0] + "\n"
	lists += "[" + str(len(list) + 1) + "]" + " Main Menu\n"
	print("Suggested Topics:\n" + lists)
	topic = int(input("Enter choice: "))
	
	print()
	if topic == len(list) + 1:
		welcome(False)
	else:
		select(int(list[topic - 1][1]) + 1)

def exit():
	msg = "Thank you for using my Program " + user + ",\n- Truly yours, Ryann Kim Sesgundo of BSIT 1A"
	for x in range(len(msg)):
		printing_(msg, x)

def printing_(txt, x):
	print(txt[x], end="", flush=True)
	delay = 1000
	y = 0
	while y < delay:
		y += 0.01

def printing():
	printer = "print() function in python is just printing or showing a string or text, or even other datatypes. This is commonly use to see the output of a specific console program. "
	printer += "Print also has parameters, and the primary parameter for this is the output, string or any datatype to print. The sep, or the separator, and the end, or the last character in a line."
	print(printer)
	cont()
	printer = "Separator may only work, if you use comma (,) to concatinate data, by also using comma, you may also concatinate different datatypes.\n\nExample:\nprint(\"Hello\", 123, sep=\"\\n\")\n"
	printer += "Output:\nHello\n123"
	print(printer)
	cont()
	printer = "Another one is by using end, end or end line is the responsible to make separations vertically, the default value of is is \\n.\n\nExample:\nprint(\"Hello\", end=\" \")\nprint(\"World\")\n"
	printer += "Output:\nHello World"
	print(printer)
	
	list = [
		[
			menu[1],
			"1"
		],
		[
			menu[2],
			"2"
		]
	]
	close(list)

def vars():
	var = "Variables are the data holder in programming. They are the representatives, or the keys to get the value of the specific data that programmer added, or the user inserted."
	print(var)
	cont()
	var = "There are many ways to make a variable, you may use cammelCases or with under_score or even with number123. But remember, you may only use underscore (_) in symbols, you may also use numbers in the middle or at the end of the variable name. Always remember to use ALL_CAPITAL_TEXT if you're going make a constant variable. \nHere's the example of using variables.\n\nvariableName = \"Hello World\"\nprint(variableName)\n\nAnother Example:\nyourName = input(\"What's your name?\")\nprint(\"Hello\", yourName)"
	print(var)
	
	list = [
		[
			menu[2],
			"2"
		],
		[
			menu[3],
			"3"
		],
		[
			menu[5],
			"5"
		]
	]
	close(list)

def operators():
	printer = "There are four different types of operator in Programming: Arithmetic, Relational, Logical. and Assignment Operator."
	print(printer)
	cont()
	
	printer = "In Arithmetic Operators, it is the operators that are commonly used in mathematical equations. Now, lets try it.\n"
	print(printer)
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	while(num1 == num2):
		num2 = int(input("Please enter another number: "))
	
	printer = "Addition: (first + second): " + str(num1 + num2) + "\n"
	printer += "Subtraction (first - second): " + str(num1 - num2) + "\n"
	printer += "Multiplication (first * second): " + str(num1 * num2) + "\n"
	printer += "Division (first / second): " + str(num1 / num2) + "\n"
	printer += "Modulo or Remainder (first % second): " + str(num1 % num2) + "\n"
	printer += "Exponentation  (first ** second): " + str(num1 ** num2) + "\n"
	printer += "Floor Division (first // second): " + str(num1 // num2)
	print(printer)
	cont()
	
	printer = "Next one is the relational operators. Basically, these operators are just going to compare two same datatypes, commonly integer or float, and returns as boolean. Now, lets try it.\n"
	print(printer)
	num1 = int(input("Enter a number: "))
	num2 = int(input("Enter another number: "))
	while(num1 == num2):
		num2 = int(input("Please enter another number: "))
	
	num3 = int(input("Enter same number either first number or second number: "))
	while num1 != num3 and num2 != num3:
		num3 = int(input("This must be same number as the first number or second number: "))
	
	printer = "Greater than (first > second): " + str(num1 > num2) + "\n"
	printer += "Less than (first < second): " + str(num1 < num2) + "\n"
	printer += "Greater than or equal (first >= third): " + str(num1 >= num3) + "\n"
	printer += "Greater than or equal (second >= third): " + str(num2 >= num3) + "\n"
	printer += "Less than or equal (first <= third): " + str(num1 <= num3) + "\n"
	printer += "Less than or equal (second == third): " + str(num1 <= num3) + "\n"
	printer += "Equals to (first == third): " + str(num1 == num3) + "\n"
	printer += "Equals to (second == third): " + str(num2 == num3)
	print(printer)
	cont()
	
	printer = "Next one is the Logical Operators. In some languages, they use && as and, || as or, and ! as not. This operators are commonly use in conditional statement, this returns as boolean value that is required in conditioning.\n"
	printer += "These are the example of using it.\n"
	printer += "True and True: " + str(True and True) + "\n"
	printer += "True and False: " + str(True and False) + "\n"
	printer += "False and False: " + str(False and False) + "\n"
	printer += "True or True: " + str(True or True) + "\n"
	printer += "True or False: " + str(True or False) + "\n"
	printer += "False or False: " + str(False or False) + "\n"
	printer += "not True: " + str(not True) + "\n"
	printer += "not False: " + str(not False)
	print(printer)
	cont()
	
	printer = "Now, we all know the first 3 operators. now, let us know about the last one. This must be the most important part of the programming. If there's about variable, we've must have Assignment Operator. This is just giving or assigning a variable to have a value. The symbols for this operators are = and other arithmetic operators with = sign such as +=, -=, *=, /=, %=, **=, //=, which I actually called as shorthand operators. But in some language, only +=, -=, *=, /= and %=, Now Let's do have some excercise to thus program."
	printer += ""
	print(printer)
	print()
	
	first = int(input("Come on, give me some number: "))
	print("The value of integer number is", first)
	print()
	second = int(input("Now, give me another number to repeat this: "))
	print("Good, the value to loop the number is", second)
	print("I'm going to initiate some integers for the output...")
	
	sum = first
	diff = first
	prod = first
	quot = first
	mods = first
	expo = first
	floorDiv = first
	
	printer = ""
	
	for i in range(second):
		
		sum += first
		diff -= first
		prod *= first
		quot /= first
		mods %= first
		expo **= first
		floorDiv //= first
		
		printer += "First number re-assigned as (+=): " + str(sum) + "\n"
		printer += "First number re-assigned as (-=): " + str(diff) + "\n"
		printer += "First number re-assigned as (*=): " + str(prod) + "\n"
		printer += "First number re-assigned as (/=): " + str(quot) + "\n"
		printer += "First number re-assigned as (%=): " + str(mods) + "\n"
		printer += "First number re-assigned as (**=): " + str(expo) + "\n"
		printer += "First number re-assigned as (/=): " + str(floorDiv) + "\n"
	
	print(printer)
	list = [
		[
			menu[4],
			"4"
		],
		[
			menu[6],
			"6"
		],
		[
			menu[7],
			"7"
		]
	]
	close(list)

def conditional():
	printer = "Conditional statement. For me, this program is one of the core of a simple project, this is a part of programming where the program will decide based on what the programmer's programmed."
	print(printer)
	cont()
	printer = "As mentioned, this is the part of the program wherein you can make your program more dynamic and decide like a human being. There a three keywords that you've might used. Thr first one is if, the most required part of conditional statement. I already created a program, and this will give you the result, the program is:\n\ndropName = input(\"Please enter a name: \")\nif dropName == user:\n\tprint(\"Hello\", dropName)\n\nWherein user is the variable name that holds your name thay you dropped in."
	print(printer)
	dropName = input("Please enter a name: ")
	if user == dropName:
		print("Hello", dropName)
	print("Program executed...")
	
	cont()
	
	printer = "The second one is by using else. This one is just optional, and can only use if you're exprecting sa catch or a return if all conditions are false. I'm going to use same code and I only add else:\n\ndropName = input(\"Please enter a name: \")\nif dropName == user:\n\tprint(\"Hello\", dropName)\nelse:\n\tprint(\"You're not\", user)\n\n"
	print(printer)
	
	dropName = input("Please enter a name: ")
	if user == dropName:
		print("Hello", dropName)
	else:
		print("You're not", user)
	print("Program executed...")
	
	cont()
	
	printer = "Lastly is using elif or combined else and if. This is like a catch of thr first if or first elifs that are False. I'm going to use again the code earlier and just modify it. \n\ndropName = input(\"Please enter a name: \")\nif dropName == user:\n\tprint(\"Hello\", dropName)\nelif dropName == \"\":\n\tprint(\"It is a blank\")\nelse:\n\tprint(\"You're not\", user)\n\n"
	print(printer)
	
	dropName = input("Please enter a name: ")
	if user == dropName:
		print("Hello", dropName)
	elif dropName == "":
		print("Its blank")
	else:
		print("You're not", user)
	print("Program executed...\n")
	
	cont()
	print("Conditional statements always requires boolean results or return to work in. This is one of the main use of boolean in a project or in a program.")
	
	cont()
	print("Let's try a program called leap year.")
	yr = int(input("Please enter a year"))
	
	if yr >= 1000 and yr % 4 == 0:
		print("The year", yr, "is a leap year.")
	elif yr < 1000:
		print("Must be a year.")
	else:
		print("The year", yr, "is not a leap year.")
	
	list = [
		[
			menu[1],
			"1"
		],
		[
			menu[4],
			"4"
		],
		[
			menu[6],
			"6"
		]
	]
	close(list)

def loop():
	printer = "Looping is doing a repeated task in a specific counts, or in a False boolean result condition. This may help a lot to do so many prints in just 2 lines of code in Python. Now, let's try this code below.\n\nfor i in range(10):\n\tprint(i)"
	print(printer)
	cont()
	
	for i in range(10):
		print(i)
	
	cont()
	
	printer = "As you notice, the loop starts with zero, and ends with 9 instead of 10, which uses the operator or relational operator <. The range function is may use to this kind of loop, which is the for loop."
	print(printer)
	cont()
	
	printer = "Next one is the another type of loop, which is the while loop. This loop is kinda using of if condition, meaning to say, this requires a boolean to continue or to loop. Here's the example:\n\ni = 0\nwhile i <= 10:\n\tprint(i)\n\ti += 1"
	print(printer)
	
	i = 0
	while i <= 10:
		print(i)
		i += 1
	
	cont()
	
	printer = "As you see, the program prints from 0 to 10 numbers, because of the operator <=. If the condition hits False, the program will be terminated. But it is not just using boolean here in looping, specially in while loop, we may also use break, to stop the program, and continue, to make an skip. Here's the example of using break.\n\ni = 0\nwhile i <= 10:\n\tprint(i)\n\tif i % 5 == 0 and i != 0:\n\t\tbreak\n\ti += 1"
	print(printer)
	
	i = 0
	while i <= 10:
		print(i)
		if i % 5 == 0 and i != 0:
			break
		i += 1
	
	cont()
	print("As you can see, the program stops on the fifth number or index, which is divisible by five, but not equal to zero.")
	cont()
	printer = "Now, let's try to use continue. i = 0\nwhile i <= 10:\n\ti += 1\n\tif i % 5 == 0 and i != 0:\n\t\tcontinue\n\tprint(i)"
	print(printer)
	
	i = 0
	while i <= 10:
		i += 1
		if i % 5 == 0 and i != 0:
			continue
		print(i)
	
	print("As you can see, the numbers thatbare divisible by 5 and not equal to zero didn't show up, that means to skip. I try so many trial and error for this, and I encounter a logic error, so the continue must placed on the last part of the program, before the print just like the code. Or else, printing will continue endlessly.")
	
	cont()
	print("Let's try to use this loop to generate a arrow up..")
	
	h = 10
	arrow = ""
	for i in range(1, h + 1):
		if i < h // 1.3:
			for j in range(((h // 2) + 1) - i):
				arrow += " "
			for j in range(i):
				arrow += "* "
		else:
			for j in range((h) // 3):
				arrow += " "
			for j in range(4):
				arrow += "* "
		arrow += "\n"
		
	print(arrow)
	
	list = [
		[
			menu[1],
			"1"
		],
		[
			menu[3],
			"3"
		],
		[
			menu[6],
			"6"
		]
	]
	close(list)

def callMe():
	print("Hello")

def sum(a, b):
	return a + b

def func():
	print("There are two types of function, the built-in functions and the user defined functions. Also, there are two ways to use a function, first one is calling functions just like using print, and return functions, which giving back a value or data from the function. Example of calling function is:\n\ndef callMe():\n\tprint(\"Hello\")\ncallMe()")
	print()
	
	callMe()
	
	cont()
	print("Next one is by having a return function. This kind of function uses return keyword with an expected data like this:\n\ndef sum(a, b):\n\treturn a + b\n\nprint(sum(1, 2))")
	print()
	
	print(sum(1, 2))
	
	cont()
	print("Function may help you to shorten your codes and makes multiple use in a same codes, which is called as code reusability.")
	
	cont()
	
	print("Now, let's try to use some of the built-in function, aside of print() as having its own explanation and definition. There are lots of built-in functions in python, but I'm just going to tackle about: len(), str(), int(), eval(), range(), input()")
	
	cont()
	
	print("Length or len(). This built-in function must contain a single parameter, either string or array. This has an integer return value, which gives you the total characters of a string, or total data of an array. Here's some example:\n\ntxt = \"Hello\"\nprint(len(txt))\n")
	
	txt = "Hello"
	print(len(txt))
	
	cont()
	print("Next one is str(). String function converts any data type into string, this helps you specially to concatinate 2 different datatypes such as string and integer. Here's the example of it:\n\nprint(\"10 ** 2 = \" + str(10 ** 2))\n")
	
	print("10 ** 2 = " + str(10 ** 2))
	
	cont()
	print("Next is Integer function or int(). This function converts a numerical value in a string form into an integer form. A character or text to integer turns to an error, that means invalid. Let's try it.\n\nval = \"10\"\nprint(int(val) + 5)\n")
	
	val = "10"
	print(int(val) + 5)
	
	cont()
	print("Next is evaluation function or eval(). Unlike of int(), this function converts a fomula or mathematical computation and return as integer datatype. Let's have some test.\n\nprint(eval(\"7 + 7 - 7 / 7 * 0\"))\n")
	
	print(eval("7 + 7 - 7 / 7 * 0"))
	
	cont()
	
	print("Next is the range(). This function is commonly use in loop. These has 1 required parameters, and 2 optional paramaters. The required parameter for this function is the stopping point, while the start and step are just optional. The step parameter must have start, or else, it will going to a logic error. If you want to try, just check out the looping menu.")
	
	cont()
	print("Lastly, the input(). This function ask user to have data, just like what I did earlier, I asked your name.")
	
	list = [
		[
			menu[1],
			"1"
		],
		[
			menu[4],
			"4"
		],
		[
			menu[6],
			"6"
		]
	]
	close(list)

def arrays():
	print("Arrays are the list or compillation of data with same datatype. It is commonly call the value through the index number or its position in array.")
	cont()
	print("Here's the example of array:\n\narr = [1, 2, 3, 4, 5]")
	cont()
	print("Now, let's try to apply the array in a program.\n\narr = [1, 2, 3, 4, 5]\nprint(\"Called by Index of 3:\",arr[3])\nprint(\"Printing all data:\", arr)")
	cont()
	
	arr = [1, 2, 3, 4, 5]
	print("Called by Index of 3:", arr[3])
	print("Printing all data:", arr)
	
	cont()
	
	print("We may also insert data in an array through append function. Now let's try the code below:\n\narr = []\ndata = input(\"Enter something: \")\nwhile data != \"\":\n\tarr.append(data)\n\tdata = input(\"Enter another data or let it blank: \")\n")
	
	arr = []
	data = input("Enter something: ")
	while data != "":
		arr.append(data)
		data = input("Enter another data or let it blank: ")
	
	print(arr)
	
	cont()
	
	print("We may remove a data in an array by using pop() function. Example:\n\narr = [1, 2, 3, 4, 5]\narr.pop()\nprint(arr)\n")
	
	arr = [1, 2, 3, 4, 5]
	arr.pop()
	print(arr)
	
	cont()
	
	print("So now, let's try to sort different integers using loop and condition.")
	
	cont()
	
	nums = []
	num = int(input("Please enter a number: "))
	while num > 0 or len(nums) < 2:
		if num < 0:
			num *= 1
		nums.append(num)
		num = int(input("Please enter a number or enter 0 or negative number to terminate: "))
	
	print("The data gathered was:", nums)
	print("Now let's sort them out.")
	
	for i in range(len(nums)):
		for j in range(i):
			if nums[i] < nums[j]:
				k = nums[i]
				nums[i] = nums[j]
				nums[j] = k
	
	print("The sorted value are:", nums)
	
	list = [
		[
			menu[1],
			"1"
		],
		[
			menu[3],
			"3"
		],
		[
			menu[4],
			"4"
		],
		[
			menu[7],
			"7"
		]
	]
	close(list)

def dictionary():
	print("Dictionary is same as the json for those who familiar with. Dictionary comes the idea from a websters which needs to use a keyword to get the definition of it.")
	cont()
	print("Here's the example of using dictionary:\n\ndiction = {\n\t\"keyword\": \"definition\"\n}\nprint(diction[\"keyword\"])\n")
	
	diction = {
		"keyword": "definition"
	}
	print(diction["keyword"])
	
	cont()
	print("Unlike array, we use {} or curly braces to have a data, and use the key or keyword to get the definition or value of that particular data ")
	list = [
		[
			menu[1],
			"1"
		],
		[
			menu[3],
			"3"
		],
		[
			menu[5],
			"5"
		]
	]
	close(list)

def select(choice):
	if choice > 0 and choice < 10:
		print("You choose:", menu[choice - 1])
	if choice == 1:
		printing()
	elif choice == 2:
		vars()
	elif choice == 3:
		operators()
	elif choice == 4:
		conditional()
	elif choice == 5:
		loop()
	elif choice == 6:
		func()
	elif choice == 7:
		arrays()
	elif choice == 8:
		dictionary()
	elif choice == 9:
		exit()
	else:
		print("Invalid Choice")
		c = int(input("Please enter a number of your choice: "))
		select(c)

def welcome(isFirst):
	menus = ""
	for i in range(len(menu)):
		menus += "[" + str(i + 1) + "] " + menu[i] + "\n"
	
	print()
	
	if isFirst:
		wc = "Welcome " + user + "! Here are the menu for fundamentals of Python\n"
		for x in range(len(wc)):
			printing_(wc, x)
		for i in range(len(menu)):
			print("[" + str(i + 1) + "] " + menu[i])
			delay = 1000
			j = 0
			while j < delay:
				j += 0.01
	else:
		print("Welcome back " + user, "! Here are the menu for fundamentals of Python\n" + menus)
	
	choice = int(input("Please enter a number of your choice: "))
	print()
	
	select(choice)

welcome(True)