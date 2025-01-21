import random
import string
from datetime import datetime

def generate_password(length, use_uppercase, use_numbers, use_specials):
    """
    Generate a secure random password based on user preferences.
    """
    # Define character pools
    character_pool = string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_specials:
        character_pool += string.punctuation

    # Ensure the password contains at least one of each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_specials:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length
    password += random.choices(character_pool, k=length - len(password))
    random.shuffle(password)  # Shuffle to avoid predictable patterns

    return ''.join(password)

def password_strength(password):
    """
    Evaluate the strength of a password based on its length and character diversity.
    """
    if len(password) < 8:
        return "Weak"
    elif len(password) >= 8 and len(set(password)) > 5:
        return "Medium"
    elif len(password) >= 12:
        return "Strong"
    return "Weak"

def save_password(password, strength):
    """
    Save the generated password to a file with a timestamp and strength indicator.
    """
    try:
        with open("saved_passwords.txt", "a") as file:
            file.write(f"{password} - Strength: {strength} - Generated on {datetime.now()}\n")
        print("Password saved to 'saved_passwords.txt'.")
    except Exception as e:
        print(f"Error saving password: {e}")

def main():
    """
    Main function to interact with the user and run the password generator.
    """
    print("Welcome to the Enhanced Password Generator!")
    try:
        # Get user preferences
        length = int(input("Enter the desired password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4.")
            return

        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        use_specials = input("Include special characters? (yes/no): ").strip().lower() == "yes"

        # Generate password
        password = generate_password(length, use_uppercase, use_numbers, use_specials)
        strength = password_strength(password)
        print(f"Generated password: {password} (Strength: {strength})")

        # Save password
        save_option = input("Would you like to save this password? (yes/no): ").strip().lower()
        if save_option == "yes":
            save_password(password, strength)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
