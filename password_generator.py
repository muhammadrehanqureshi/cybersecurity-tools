import random
import string

def generate_password(length, use_uppercase, use_numbers, use_specials):
    # Define character pools
    character_pool = string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_specials:
        character_pool += string.punctuation
    
    # Ensure password contains at least one of each selected type
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

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4.")
        else:
            use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
            use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
            use_specials = input("Include special characters? (yes/no): ").strip().lower() == "yes"
            
            password = generate_password(length, use_uppercase, use_numbers, use_specials)
            print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
