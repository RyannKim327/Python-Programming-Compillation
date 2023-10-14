import random

def create():
	pronoun = [
		"He is",
		"She is",
		"They are",
		"I am",
		"We are"
	]
	verb = [
		"walking",
		"dancing",
		"running",
		"singing"
	]
	a = random.randint(0, len(pronoun) - 1)
	b = random.randint(0, len(verb) - 1)
	return f"{pronoun[a]} {verb[b]}."

print(create())