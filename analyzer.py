import re
import math
import random
import bcrypt
def check_password(password):
    length = len(password)

    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[@$!%*?&]", password))

    score = 0

    if length >= 8:
        score += 1

    if length >= 12:
        score += 1

    if has_lower:
        score += 1

    if has_upper:
        score += 1

    if has_digit:
        score += 1

    if has_symbol:
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Moderate"

    else:
        return "Strong"

def calculate_entropy(password):

    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26

    if re.search(r"[A-Z]", password):
        charset += 26

    if re.search(r"[0-9]", password):
        charset += 10

    if re.search(r"[@$!%*?&]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)

    return round(entropy, 2)
def is_common_password(password):

    with open("common.txt", "r") as file:

        common_passwords = file.read().splitlines()

    return password.lower() in common_passwords
def has_pattern(password):

    patterns = [
        "123",
        "abc",
        "qwerty",
        "admin",
        "password"
    ]

    password = password.lower()

    for pattern in patterns:

        if pattern in password:
            return True

    return False
def suggest_password():

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "@#$&!*"

    all_characters = uppercase + lowercase + numbers + symbols

    password = ""

    password += random.choice(uppercase)
    password += random.choice(lowercase)
    password += random.choice(numbers)
    password += random.choice(symbols)

    for i in range(8):
        password += random.choice(all_characters)

    password_list = list(password)

    random.shuffle(password_list)

    final_password = "".join(password_list)

    return final_password
def hash_password(password):

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    return hashed.decode()
def verify_password(password, hashed_password):

    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )

if __name__ == "__main__":

    password = input("Enter password: ")

    result = check_password(password)

    print("Password Strength:", result)

    entropy = calculate_entropy(password)

    print("Entropy:", entropy, "bits")

    if is_common_password(password):
        print("⚠ WARNING: This is a common password!")

    if has_pattern(password):
        print("⚠ WARNING: Predictable pattern detected!")

    print("Suggested Strong Password:", suggest_password())

    hashed_password = hash_password(password)

    print("Hashed Password:", hashed_password)

    verification = verify_password(
        password,
        hashed_password
    )

    print("Password Match:", verification)