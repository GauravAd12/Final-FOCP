# 2. Write a program that, when run from the command line, reports how many
# arguments were provided. (Remember that the program name itself is not an
# argument).

import sys

# Exclude the program name
argument_count = len(sys.argv) - 1
print(f"Number of arguments: {argument_count}")
