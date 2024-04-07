def printPine(height, count):
    r = ""
    l = 0
    for i in range(1, height + 1):
        r += ((" " * (height - i) + "*" * (l + i) + " " * (height - i) + " ") * count) + "\n"
        l = i
    return r

print(printPine(10, 3))
