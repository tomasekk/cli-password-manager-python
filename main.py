# programmed by
#   linkedin.com/in/ondrat
#   github.com/tomasekk

import os
import random
import string

PASSWORDS_FILE = "passwds/passwords.txt"

def generate_password(length=12):
    """Generate a random password of specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def add_password():
    """Add a new password to the password manager"""
    website = input("Enter website name: ")
    username = input("Enter username: ")
    cstm_or_random = input("Generate random password (0) or add custom one (1)?: ")
    while True:
        if cstm_or_random == "1":
            password = input("Enter password: ")
            break
        elif cstm_or_random == "0":
            password = generate_password()
            break
        else:
            print("Enter 0 or 1")
            pass
    with open(PASSWORDS_FILE, "a") as f:
        f.write(f"{website},{username},{password}\n")
    print("Password added successfully!")

def get_password():
    """Retrieve a password from the password manager"""
    website = input("Enter website name: ")
    with open(PASSWORDS_FILE, "r") as f:
        for line in f:
            line = line.strip().split(",")
            if line[0] == website:
                print("Username:", line[1])
                print("Password:", line[2])
                return
        print("Password not found for that website.")

def list_passwords():
    """Retrieve all domains from the password manager"""
    with open(PASSWORDS_FILE, 'r') as f:
        first_line = f.readline()
        first_domain = first_line.split(',')[0]
        print(first_domain)

def main():
    # Check if password file exists, create it if it doesn't
    if not os.path.exists("passwds"):
        os.mkdir("passwds")
    if not os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, "w") as f:
            f.write("")
    # Main loop
    while True:
        print("\nPassword Manager\n")
        print("1. Add a password")
        print("2. Get a password")
        print("3. Show saved domains")
        print("4. Quit")
        choice = input("\nEnter your choice (1-4): ")
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            list_passwords()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
