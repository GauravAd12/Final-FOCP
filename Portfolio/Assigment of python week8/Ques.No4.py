
# 4. The Unix wc command counts the number of lines, words, and characters in a file.
# Write an implementation of this that takes a file name as a command-line
# argument, and then prints the number of lines and characters.

import sys

def wc_command(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_chars = sum(len(line) for line in lines)
            num_words = sum(len(line.split()) for line in lines)
            
            # Output the results
            print(f"Number of Lines: {num_lines}")
            print(f"Number of Words: {num_words}")
            print(f"Number of Characters: {num_chars}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found. Please check the file name and try again.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc_command.py <file_name>")
    elif sys.argv[1] == sys.argv[0]:
        print("Error: Cannot process the script itself. Please provide a different file name.")
    else:
        wc_command(sys.argv[1])