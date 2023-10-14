import time

def cd(t: int = 60):
	while t:
		mins, secs = divmod(t, 60)
		print("{:02d}:{:02d}".format(mins, secs), end="\r")
		time.sleep(1)
		t -= 1
	print("Time is up")

n = input("Please enter a number: ")
try:
	t = int(n)
	cd(t)
except:
	print("This is not a number")