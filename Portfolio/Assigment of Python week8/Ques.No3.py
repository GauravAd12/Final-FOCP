# 3. The Unix grep command searches a file and outputs the lines in the file that
# contain a certain pattern. Write an implementation of this. It will take two
# command-line arguments: the first is the string to look for, and the second is the
# file name. The output should be the lines in the file that contain the string.

import sys

def grep_command(pattern, file_name):
    """
    Searches a file for lines containing a certain pattern.

    Args:
        pattern (str): The pattern to search for.
        file_name (str): The name of the file to search.

    Returns:
        None
    """
    try:
        with open(file_name, 'r') as file_obj:
            found = False
            for line in file_obj:
                if pattern in line:
                    print(line.strip())
                    found = True
            if not found:
                print(f"No lines found containing the pattern '{pattern}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Please check the file name and try again.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python Ques.No2.py <pattern> <file_name>")
    else:
        grep_command(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
