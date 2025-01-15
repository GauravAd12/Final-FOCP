# 3. Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name dierently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.
def greet(name):
    formatted_name = name.capitalize()  # Capitalizes the first letter and lowers the rest
    return f"Hello, {formatted_name}!"

# Testing the function
print(greet("Gaurav"))  # Hello, Arthur!
print(greet("GAURAV"))  # Hello, Gaurav!
print(greet("GAurAv"))  # Hello, Gaurav!
