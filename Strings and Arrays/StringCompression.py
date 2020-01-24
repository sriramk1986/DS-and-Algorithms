def string_compression(input_str):
    compressed = []
    counter = 0

    for i in range(len(input_str)):
        if i != 0 and input_str[i] != input_str[i - 1]:
            compressed.append(input_str[i - 1] + str(counter))
            counter = 0
        counter += 1

    compressed.append(input_str[-1] + str(counter))
    return min(input_str, "".join(compressed), key=len)


print(string_compression("abcdef"))

# Takeaways:
# 1. How to solve the problem of checking for the last letter. 
# By not checking it in the loop and adding it post the completion of the loop
