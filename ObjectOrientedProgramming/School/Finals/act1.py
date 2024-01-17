def devide_numbers():
	while True:
		try:
			num1 = float(input("Please enter number 1: "))
			num2 = float(input("Please enter number 2: "))
			print(f"{num1} divided by {num2} is {num1 / num2}")
			break
		except ValueError as e:
			print("Invalid input, kindly enter a number")
		except ZeroDivisionError as e:
			print("The first number won't divide to zero")
		except:
			print("Basta may error prii")
		finally:
			print("Ahhhhhhh successssssss")

devide_numbers()