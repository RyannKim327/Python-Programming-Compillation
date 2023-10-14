from time import time

def check(act):
	start = time()
	act()
	print(f"Time: {time() - start}")