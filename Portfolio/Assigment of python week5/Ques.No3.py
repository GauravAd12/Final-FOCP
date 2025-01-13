
# 3. Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them.



import sys

if len(sys.argv) <= 1:
    print("No arguments provided.")
else:
    # Exclude the program name
    arguments = sys.argv[1:]
    shortest = min(arguments, key=len)
    print(f"Shortest argument: {shortest}")
