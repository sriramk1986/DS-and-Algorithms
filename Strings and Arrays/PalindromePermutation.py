def palindromePermutation(input_str):
    string_chars = {}
    input_str = format_string(input_str)

    for char in input_str:
        if char in string_chars:
            string_chars[char] += 1
        else:
            string_chars[char] = 1

    print(string_chars)
    odd_count = 0
    for _key, value in string_chars.items():
        if value % 2 == 1:
            odd_count += 1
    print(odd_count)
    return odd_count <= 1


def format_string(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()
    return input_str


print(palindromePermutation("azAZ"))

# Takeaways:
# 1. Iterate through dict using key and values by using dict.items()
# 2. Could have also used ord(char) for getting ascii value and then populating an array of range 26
# set all the values to zero and then increment based on the letter. Compare count of odds.
