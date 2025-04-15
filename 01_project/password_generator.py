import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_symbols=True):
    """
    Generate a random password with specified characteristics
    
    Args:
        length: Length of the password (default: 12)
        include_uppercase: Whether to include uppercase letters (default: True)
        include_digits: Whether to include digits (default: True)
        include_symbols: Whether to include special symbols (default: True)
        
    Returns:
        A randomly generated password string
    """
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if include_uppercase else ""
    digit_chars = string.digits if include_digits else ""
    symbol_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/" if include_symbols else ""
    
    # Combine all character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + symbol_chars
    
    # Ensure minimum length
    if length < 4:
        length = 4
        print("Minimum password length is 4. Setting length to 4.")
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter password length (default: 12): ") or "12")
        
        include_uppercase = input("Include uppercase letters? (y/n, default: y): ").lower() != 'n'
        include_digits = input("Include digits? (y/n, default: y): ").lower() != 'n'
        include_symbols = input("Include symbols? (y/n, default: y): ").lower() != 'n'
        
        # Generate and display password
        password = generate_password(
            length=length,
            include_uppercase=include_uppercase,
            include_digits=include_digits,
            include_symbols=include_symbols
        )
        
        print("\nGenerated Password:")
        print("-------------------")
        print(password)
        print("-------------------")
        
        # Save to file option
        save_option = input("\nSave this password to a file? (y/n): ").lower()
        if save_option == 'y':
            description = input("Enter a description for this password: ")
            with open("passwords.txt", "a") as file:
                file.write(f"{description}: {password}\n")
            print("Password saved to passwords.txt")
        
    except ValueError:
        print("Invalid input. Using default values.")
        password = generate_password()
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main() 