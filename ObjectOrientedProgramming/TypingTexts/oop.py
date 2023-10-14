import time

def show(_str: str, speed: float = 0.1):
	for i in range(len(_str)):
		print(_str[i], end="", flush=True)
		time.sleep(speed)

def have(_prompt: str, speed: float = 0.1):
	for i in range(len(_prompt)):
		print(_prompt[i], end="", flush=True)
		time.sleep(speed)
	if(_prompt.endswith(":  ")):
		return input()
	else:
		return input(": ")