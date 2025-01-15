# 4. When processing data it is oen useful to remove the last character from some
# input (it is oen a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)
def remove_last_character(s):
    return s[:-1] if len(s) > 1 else s

# Testing the function
print(remove_last_character("Namasta!"))  # Namasta
print(remove_last_character("A"))       # A
print(remove_last_character(""))        # (unchanged)
