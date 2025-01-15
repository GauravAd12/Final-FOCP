# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password1 = input("Enter a new password (8-12 characters): ")
if 8 <= len(password1) <= 12:
    if password1 not in BAD_PASSWORDS:
        password2 = input("Re-enter your password: ")
        if password1 == password2:
            print("Password Set")
        else:
            print("Error: Passwords do not match!")
    else:
        print("Error: Password is too common!")
else:
    print("Error: Password must be between 8 and 12 characters!")
