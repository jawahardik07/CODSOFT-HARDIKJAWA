import random
import string

# Function to generate a password
def generate_password(length):
    if length < 4:
        return "Error: Password length should be at least 4 characters for complexity."

    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all sets combined
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness and convert it to a string
    random.shuffle(password)
    return ''.join(password)

# Main program loop
def main():
    while True:
        try:
            # Prompt the user to specify the desired length of the password
            length = int(input("Enter the desired length of the password (minimum 4): "))
            
            # Generate and display the password
            password = generate_password(length)
            print(f"Generated password: {password}")
            
            # Ask the user if they want to generate another password
            choice = input("Generate another password? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()

