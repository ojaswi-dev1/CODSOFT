# PASSWORD GENERATOR - TASK 3

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter the desired password length: "))

# Generate and display password
password = generate_password(length)
print("Generated Password:", password)
