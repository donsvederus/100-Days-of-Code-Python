import random

# List of all lowercase letters in the alphabet
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# List of all numbers from 0 to 9 as strings
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# List of symbols suitable for setting passwords, excluding problematic characters
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", 
           "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?"]

# Ask the user for the total length of the password
total_length = int(input("How long would you like your password to be? "))

# Initialize an empty list to store the password characters
password_chars = []

# Ensure at least one letter, one number, and one symbol
if total_length < 3:
    print("Password length should be at least 3 to include letters, numbers, and symbols.")
else:
    num_letters = random.randint(1, total_length - 2)
    num_numbers = random.randint(1, total_length - num_letters - 1)
    num_symbols = total_length - num_letters - num_numbers

    # Select random letters
    for _ in range(num_letters):
        password_chars.append(random.choice(letters))

    # Select random numbers
    for _ in range(num_numbers):
        password_chars.append(random.choice(numbers))

    # Select random symbols
    for _ in range(num_symbols):
        password_chars.append(random.choice(symbols))

    # Shuffle the list to ensure the characters are in random order
    random.shuffle(password_chars)

    # Join the list into a single string to form the final password
    password = ''.join(password_chars)

    # Print the generated password
    print(f"Your generated password is: {password}")