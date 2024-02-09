import time
from builtins import print as __print__, input as __input__

def print(_str: str, speed: float = 0.1):
	for i in range(len(_str)):
		__print__(_str[i], end="", flush=True)
		time.sleep(speed)
	__print__()

def input(_prompt: str, speed: float = 0.1):
	for i in range(len(_prompt)):
		__print__(_prompt[i], end="", flush=True)
		time.sleep(speed)
	if _prompt.endswith(":  "):
		return __input__()
	elif _prompt.endswith(":"):
		return __input__(" ")
	else:
		return __input__(": ")