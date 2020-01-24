# Solution 1: Use a set to store unique values. Time Complexity = O(N)
def isUnique(string):
    uniqueChars = set()
    for char in string:
        if char in uniqueChars:
            return False
        uniqueChars.add(char)
    return True

# Solution 2: Check whether input is ASCII or Unicode. If ASCII, then use below solution: Time complexity: O(N)
def isUnique2(string):
    # ASCII characters are from 0 -127
    if len(string) > 128:
        return False
    
    character_set = [False for _ in range(128)]
    for char in string:
        value = ord(char)
        if character_set[value]:
            return False
        character_set[value] = True
    
    return True