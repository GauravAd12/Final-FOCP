# 2. Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.
def count_case(s):
    uppercase = sum(1 for char in s if char.isupper())
    lowercase = sum(1 for char in s if char.islower())
    return uppercase, lowercase

# Testing the function
test_string = "Hello World!"
uppercase, lowercase = count_case(test_string)
print(f"Uppercase letters: {uppercase}, Lowercase letters: {lowercase}")
