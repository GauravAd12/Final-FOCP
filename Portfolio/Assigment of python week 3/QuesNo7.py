# 7. Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.
number = int(input("Enter the number of the times table you require (0-12): "))
if 0 <= number <= 12:
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
else:
    print("Error: Number must be between 0 and 12.")
