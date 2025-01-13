
# 6. Write a program that decrypts messages encoded as above.


import random
import string

# Encryption function for reference
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

# Decryption function
def interval_decrypt(encrypted_message, interval):
    return encrypted_message[interval - 1::interval]

# Example usage
message = "send cheese"
encrypted, interval = interval_encrypt(message)
print(f"Encrypted: {encrypted}, Interval: {interval}")

decrypted = interval_decrypt(encrypted, interval)
print(f"Decrypted: {decrypted}")
