import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    if length < 8:
        return "Password length should be at least 8 characters."
    
    # Define character sets
    letters = string.ascii_letters  # Includes both lowercase and uppercase letters
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets
    all_characters = letters + digits + special_chars

    # Randomly select characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    # Prompt user for password length
    try:
        length = int(input("Enter the desired length of the password (minimum 8): "))
        if length < 8:
            print("Password length should be at least 8 characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")

# Run the password generator
if __name__ == "__main__":
    main()
