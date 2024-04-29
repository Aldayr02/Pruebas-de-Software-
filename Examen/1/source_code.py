import hashlib
import json
import os
import secrets
import string

USER_DATA_FILE = "users.json"


def generate_salt():
    """Generates a random salt."""
    return secrets.token_hex(16)


def generate_password_hash(password, salt):
    """Generates a password hash using SHA-256."""
    password_hash = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
    return password_hash


def load_user_data():
    """Loads user data from JSON file."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}


def save_user_data(data):
    """Saves user data to JSON file."""
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def register(username):
    """Registers a new user."""
    user_data = load_user_data()
    if username in user_data:
        print("User already exists. Please choose a different username.")
    else:
        password = input("Enter your password: ")
        salt = generate_salt()
        password_hash = generate_password_hash(password, salt)
        user_data[username] = {"password_hash": password_hash, "salt": salt}
        save_user_data(user_data)
        print("User registered successfully.")


def login(username, password):
    """Logs in the user."""
    user_data = load_user_data()
    if username not in user_data:
        print("User does not exist. Please register first.")
    else:
        stored_password_hash = user_data[username]["password_hash"]
        salt = user_data[username]["salt"]
        password_hash = generate_password_hash(password, salt)
        if password_hash == stored_password_hash:
            print("Login successful!")
        else:
            print("Invalid password. Please try again.")


def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            register(username)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login(username, password)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
