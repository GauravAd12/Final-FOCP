# 4. One approach to analysing some encrypted data where a substitution is suspected
# is frequency analysis. A count of the dierent symbols in the message can be used
# to identify the language used, and sometimes some of the letters. In English, the
# most common letter is "e", and so the symbol representing "e" should appear most
# in the encrypted text.

from collections import Counter

def frequency_analysis(message):
    message = message.lower()
    letter_counts = Counter(filter(str.isalpha, message))
    most_common = letter_counts.most_common(6)
    for letter, count in most_common:
        print(f"{letter}: {count}")

# Example usage
message = "This is an example message for frequency analysis!"
frequency_analysis(message)
