# 6. Write a program that takes the name of a file as a command-line argument, and
# creates a backup copy of that file. The backup should contain an exact copy of the
# contents of the original and should, obviously, have a dierent name.
import sys
import shutil

if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
else:
    original_file = sys.argv[1]
    backup_file = f"{original_file}.backup"
    try:
        shutil.copy(original_file, backup_file)
        print(f"Backup created: {backup_file}")
    except FileNotFoundError:
        print("File not found.")
    except IOError as e:
        print(f"Error: {e}")
