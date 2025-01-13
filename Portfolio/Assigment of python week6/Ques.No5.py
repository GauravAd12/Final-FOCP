# 5. Another way to hide a message is to include the letters that make it up within
# seemingly random text. The letters of the message might be every fih character,
# for example. Write and test a function that does such encryption. It should
# randomly generate an interval (between 2 and 20), space the message out
# accordingly, and should fill the gaps with random letters. The function should
# return the encrypted message and the interval used.
# For example, if the message is "send cheese", the random interval is 2, and for
# clarity the random letters are not random:
# send cheese
# s e n d c h e e s e
# sxyexynxydxy cxyhxyexyexysxye
import random
import string

def interval_encrypt(message):
    interval = random.randint(2, 20)
    encrypted_message = ""
    index = 0

    for char in message:
        while len(encrypted_message) < index + interval - 1:
            encrypted_message += random.choice(string.ascii_lowercase)
        encrypted_message += char
        index += interval

    return encrypted_message, interval

# Example:
encrypted, interval = interval_encrypt("send cheese")
print(f"Encrypted: {encrypted}, Interval: {interval}")

