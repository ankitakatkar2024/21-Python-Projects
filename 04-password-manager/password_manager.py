# ============================================================
# PROJECT 04: PASSWORD MANAGER
# ============================================================
#
# BASIC VERSION:
# - Created a simple password manager using Python.
# - Used Fernet symmetric encryption to encrypt passwords.
# - Generated and loaded an encryption key using a key file.
# - Added functionality to store and view passwords.
# - Used file handling to save encrypted passwords.


# from cryptography.fernet import Fernet

# # def write_key():
# #     key = Fernet.generate_key()
# #     with open("key.key", "wb") as key_file:
# #         key_file.write(key) 
# # write_key()

# def load_key():
#     file = open("key.key", "rb")
#     key = file.read()
#     file.close()
#     return key

# master_pwd = input("What is the master password? ")
# key = load_key()
# fer = Fernet(key)

# # key + password + text to encrypt = random text
# # random text + key + password = text to encrypt
   
# def view():
#     with open("passwords.txt", "r") as f:
#         for line in f.readlines():
#             data = line.rstrip()

#             if not data or "|" not in data:
#                 continue

#             user, passw = data.split("|", 1)

#             print(
#                 "User:", user,
#                 "| Password:", str(fer.decrypt(passw.encode()))
#             )

# def add():
#     name = input("Account Name: ")
#     pwd = input("Password: ")

#     with open("passwords.txt", "a") as f:
#         f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
   
        

# while True:
#     mode = input("Would you like to add a new password or view existing ones (view, add), press 'q' to quit: ?").lower()
#     if mode == "q":
#         break
#     elif mode == "view":
#         view()
#     elif mode == "add":
#         add()
#     else:
#         print("Invalid mode")



# UPGRADED VERSION:
# - Added master password authentication.
# - Implemented PBKDF2 key derivation.
# - Used SHA-256 hashing algorithm.
# - Added random salt generation for stronger security.
# - Implemented master password verification.
# - Improved password encryption and decryption.
# - Added input validation and error handling.
# - Improved menu-driven user interface.
#
# TECHNOLOGIES:
# Python | Cryptography | Fernet | PBKDF2 | SHA-256


import os
import base64

from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


SALT_FILE = Path("salt.key")
PASSWORD_FILE = Path("passwords.txt")
VERIFIER_FILE = Path("master.verifier")


# Generate encryption key using master password
def generate_key(master_pwd):

    if SALT_FILE.exists():
        salt = SALT_FILE.read_bytes()
    else:
        salt = os.urandom(16)
        SALT_FILE.write_bytes(salt)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000
    )

    key = base64.urlsafe_b64encode(
        kdf.derive(master_pwd.encode())
    )

    return Fernet(key)


# Verify master password
def verify_master_password(fer):

    if VERIFIER_FILE.exists():
        try:
            result = fer.decrypt(VERIFIER_FILE.read_bytes())

            if result != b"password-manager":
                return False

        except InvalidToken:
            return False

    else:
        verifier = fer.encrypt(b"password-manager")
        VERIFIER_FILE.write_bytes(verifier)

    return True


# View saved passwords
def view(fer):

    if not PASSWORD_FILE.exists():
        print("\nNo passwords saved yet.")
        return

    found = False

    with open(PASSWORD_FILE, "r") as f:

        for line in f:

            data = line.strip()

            if not data or "|" not in data:
                continue

            user, passw = data.split("|", 1)

            try:
                decrypted_password = fer.decrypt(
                    passw.encode()
                ).decode()

                print(
                    "Account:", user,
                    "| Password:", decrypted_password
                )

                found = True

            except InvalidToken:
                print("Unable to decrypt password for:", user)

    if not found:
        print("\nNo passwords found.")


# Add a new password
def add(fer):

    name = input("Account Name: ").strip()
    pwd = input("Password: ")

    if not name or not pwd:
        print("Account name and password cannot be empty.")
        return

    if "|" in name:
        print("Account name cannot contain '|'.")
        return

    encrypted_password = fer.encrypt(
        pwd.encode()
    ).decode()

    with open(PASSWORD_FILE, "a") as f:
        f.write(name + "|" + encrypted_password + "\n")

    print("Password saved successfully!")


# Main program
def main():

    print("\n========== PASSWORD MANAGER ==========")

    master_pwd = input("Enter your master password: ")

    if not master_pwd:
        print("Master password cannot be empty.")
        return

    fer = generate_key(master_pwd)

    if not verify_master_password(fer):
        print("\nIncorrect master password!")
        return

    print("\nMaster password verified successfully!")

    while True:

        mode = input(
            "\nChoose an option:\n"
            "1. Add a password\n"
            "2. View passwords\n"
            "3. Quit\n"
            "Enter your choice: "
        ).strip()

        if mode == "1":
            add(fer)

        elif mode == "2":
            view(fer)

        elif mode == "3":
            print("\nThank you for using Password Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
