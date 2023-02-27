import random

number = random.randint(1, 100)

trials = 5

guess = int(input("Guess a number from 1 to 100: "))

while trials > 0:
	if guess == number:
		print("Corrent")
		break
	elif guess > number:
		guess = int(input("Too Large: "))
	else:
		guess = int(input("Too Small: "))
	trials -= 1

if trials == 0:
	print(f"The answer is {number}")