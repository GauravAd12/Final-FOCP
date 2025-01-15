# 5. Last week you wrote a program that processed a collection of temperature readings
# entered by the user and displayed the maximum, minimum, and mean. Create a
# version of that program that takes the values from the command-line instead. Be
# sure to handle the case where no arguments are provided!


import sys

if len(sys.argv) <= 1:
    print("No temperature readings provided.")
else:
    try:
        # Convert arguments to numbers
        readings = list(map(float, sys.argv[1:]))
        print(f"Maximum: {max(readings)}")
        print(f"Minimum: {min(readings)}")
        print(f"Mean: {sum(readings) / len(readings)}")
    except ValueError:
        print("All inputs must be numbers.")
