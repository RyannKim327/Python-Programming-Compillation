import random
w = " ⬜ "
s = " ⬛ "
d = [
	s + s + s + "\n" +
	s + w + s + "\n" +
	s + s + s,

	w + s + s + "\n" +
	s + s + s + "\n" +
	s + s + w,

	w + s + s + "\n" +
	s + w + s + "\n" +
	s + s + w,

	w + s + w + "\n" +
	s + s + s + "\n" +
	w + s + w,
	
	w + s + w + "\n" +
	s + w + s + "\n" +
	w + s + w,
	
	w + s + w + "\n" +
	w + s + w + "\n" +
	w + s + w,
]

print(d[random.randint(0, len(d) - 1)])