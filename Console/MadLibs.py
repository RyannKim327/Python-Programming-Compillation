import os

name = input("Enter your name: ")
place = input("Enter your dream place: ")
job = input("Enter your dream job: ")
company = input("Enter your dream company: ")
name2 = input("Enter your crush name: ")
if "wala" in name2:
	name2 = "ay walang bebe"
else:
	name2 = "someone na hindi mapapasayo"
if os.system("cls"):
	os.system("clear")
print(f"Hello \033[32m{name}\033[37m, its been a while, when last time I saw you. One time you told me you wanna work on \033[32m{company}\033[37m in \033[32m{place}\033[37m, as a \033[32m{job}\033[37m. I hope that soon, your dream come true, just believe, and nothing is imposible.\n- Love: {name2}", flush=True)
print("\033[37m")