import re
import math

def calculate_entropy(password):
    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"[0-9]", password):
        charset_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset_size += 32

    if charset_size == 0:
        return 0

    return round(len(password) * math.log2(charset_size), 2)

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if re.search(r"(123|password|qwerty)", password.lower()):
        feedback.append("Avoid common patterns.")

    entropy = calculate_entropy(password)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, entropy, feedback

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter a password: ")

    strength, entropy, feedback = check_strength(password)

    print(f"\nStrength: {strength}")
    print(f"Entropy: {entropy} bits")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)
    else:
        print("\nGreat password!")

if __name__ == "__main__":
    main()