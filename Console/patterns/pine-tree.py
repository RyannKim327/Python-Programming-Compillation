def printPine(height):
    r = ""
    l = 0
    for i in range(1, height + 1):
        r += " " * (height - i)
        r += "*" * (l + i)
        r += "\n"
        l = i
    return r

print(printPine(10))
