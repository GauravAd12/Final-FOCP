# 5. Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the password the first time.
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password (8-12 characters): ")
    if 8 <= len(password1) <= 12:
        if password1 not in BAD_PASSWORDS:
            password2 = input("Re-enter your password: ")
            if password1 == password2:
                print("Password Set")
                break
            else:
                print("Error: Passwords do not match! Try again.")
        else:
            print("Error: Password is too common! Try again.")
    else:
        print("Error: Password must be between 8 and 12 characters! Try again.")
