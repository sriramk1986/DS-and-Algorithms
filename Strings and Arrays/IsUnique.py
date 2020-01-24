def isUnique(string):
    uniqueChars = set()
    for char in string:
        if char in uniqueChars:
            return False
        uniqueChars.add(char)
    return True

# print(isUnique("repeat"))