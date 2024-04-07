def generateDiamond(height, duplication = 2):
    r = ""
    l = 0
    for i in range(1, height + 1):
        r += (((" " * (height - i)) + ("*" * (i + l)) + (" " * (height - i)) + " ") * duplication) +  "\n"
        l = i
    l = height
    for i in range(height - 1, -1, -1):
        r += (((" " * (height - i)) + ("*" * ((i + l) - 2)) + (" " * (height - i)) + " ") * duplication) + "\n"
        l = i
    return r

def invertedPy(height):
    r  = ""
    l = height
    for i in range(height - 1, - 1, -1):
        print(height - i)
        r += ((" " * (height - i)) + ("*" * ((l + i) - 2))) + "\n"
        l = i
    return r

# print(invertedPy(5))
print(generateDiamond(5, 5))
