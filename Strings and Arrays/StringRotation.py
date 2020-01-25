def is_substring(string, sub):
    return string.find(sub) != -1


def string_rotation(s1, s2):
    if len(s1) == len(s2):
        return is_substring(s1 + s1, s2)
    return False


print(string_rotation("waterbottle", "erbottlewat"))

