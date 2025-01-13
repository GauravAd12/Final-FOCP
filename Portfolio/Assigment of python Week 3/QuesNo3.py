# 3. Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.

password1 = input("Enter a new password (8-12 characters): ")
if 8 <= len(password1) <= 12:
    password2 = input("Re-enter your password: ")
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match!")
else:
    print("Error: Password must be between 8 and 12 characters!")
