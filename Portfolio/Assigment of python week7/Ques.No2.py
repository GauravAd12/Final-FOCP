# 2. Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both

def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))

def letters_in_one_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))

# Example usage
word1 = "hello"
word2 = "world"

print(letters_in_either(word1, word2))  # Output: ['d', 'e', 'h', 'l', 'o', 'r', 'w']
print(letters_in_both(word1, word2))   # Output: ['l', 'o']
print(letters_in_one_not_both(word1, word2))  # Output: ['d', 'e', 'h', 'r', 'w']
