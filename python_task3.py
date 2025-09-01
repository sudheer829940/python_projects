import random
import string

print("Welcome to the Password Generator!")

while True:
    length_input = input("Enter the length of the password you want: ").strip()
    if length_input.isdigit() and int(length_input) > 0:
        password_length = int(length_input)
        break
    else:
        print("Please enter a valid positive number.")

use_letters = input("Include letters? (yes/no): ").strip().lower()
use_digits = input("Include numbers? (yes/no): ").strip().lower()
use_symbols = input("Include symbols? (yes/no): ").strip().lower()

letters = string.ascii_letters if use_letters == "yes" else ""
digits = string.digits if use_digits == "yes" else ""
symbols = string.punctuation if use_symbols == "yes" else ""

all_chars = letters + digits + symbols

if not all_chars:
    print("No character types selected! Generating default letters-only password.")
    all_chars = string.ascii_letters

password = "".join(random.choice(all_chars) for _ in range(password_length))

print("\nYour generated password is:")
print(password)