a = int(input("Enter a number: "))

match(a):
	case 1:
		print("Hello")
	case 2:
		print("World")
	case _:
		print("Default")