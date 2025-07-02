import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        user_input = int(input("Enter desired password length: "))
        if user_input <= 0:
            print("Please enter a positive number.")
            return
        password = generate_password(user_input)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
