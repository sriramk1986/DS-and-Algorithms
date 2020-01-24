def one_away(str1, str2):
    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)
    elif len(str1) - len(str2) == 1:
        return one_edit_insert(str2, str1)
    elif len(str2) - len(str1) == 1:
        return one_edit_insert(str1, str2)
    return False


def one_edit_replace(str1, str2):
    difference = False
    print(str1)
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            if difference:
                return False
            difference = True
    return True


def one_edit_insert(str1, str2):
    i, j = 0, 0
    print(str1)
    print(str2)
    difference = False
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if difference:
                return False
            difference = True
            j += 1
        else:
            i += 1
            j += 1
    return True


print(one_away("pale", "ple"))

