def urlify(string, length):
    new_index = len(string)

    for index in reversed(range(length)):
        if string[index] == " ":
            string[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            string[new_index - 1] = string[index]
            new_index -= 1
    return string


print("".join(urlify(list("Mr John Smith    "), 13)))

# takeaways:
# 1. Iterating in the reverse manner over a string when you are manipulating is useful.
# 2. Syntax of join in Python
