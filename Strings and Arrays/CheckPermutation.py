from collections import Counter

def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    string1Count = Counter(string1)
    string2Count = Counter(string2)
    if string1Count == string2Count:
        return True
    return False
    
    # Other way:
    # string1Hash = Counter()
    # for char in string1:
    #     string1Hash[char] += 1
    # for char in string2:
    #     if string1Hash[char] == 0:
    #         return False
    #     string1Hash[char] -= 1
    # return True
    
# Other things to note:
# 1. Does either string contain blank spaces
# 2. Case sensitive inputs?
# 3. Other way is to sort the strings and check if they are equal


print(checkPermutation("abc", "cab"))