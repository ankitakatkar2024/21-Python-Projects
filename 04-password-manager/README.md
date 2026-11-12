
# 🔐 Python Password Manager

A command-line Password Manager built using Python and the Cryptography library.

This project allows users to securely store, encrypt, and retrieve their passwords using Fernet symmetric encryption.

## 🚀 Features

- Master password authentication
- Password encryption and decryption
- Fernet symmetric encryption
- PBKDF2 key derivation
- SHA-256 hashing algorithm
- Random salt generation
- Add new account passwords
- View saved passwords
- Input validation
- Error handling
- Local file storage

## 🛠️ Technologies Used

- Python 3
- Cryptography
- Fernet Encryption
- PBKDF2
- SHA-256

## 📂 Project Structure

```text
04-password-manager/
│
├── password_manager.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd 04-password-manager
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the program

```bash
python password_manager.py
```

## 💻 How It Works

1. The user enters a master password.
2. PBKDF2 derives an encryption key from the master password and a randomly generated salt.
3. Fernet encrypts the account passwords.
4. Encrypted passwords are stored in a local text file.
5. The user can retrieve and decrypt saved passwords after successful master password verification.

## 📁 Automatically Generated Files

| File | Purpose |
|---|---|
| salt.key | Stores the random salt |
| passwords.txt | Stores encrypted passwords |
| master.verifier | Verifies the master password |

These files should remain private and should not be uploaded to GitHub.

## 🔒 Security Notes

- Never share your master password.
- Keep your salt and password data files safe.
- Losing the salt or forgetting the master password means losing access to saved passwords.
- This is an educational project and has not been professionally security audited.

## 📈 Future Improvements

- Delete saved passwords
- Update existing passwords
- Search for accounts
- Graphical user interface
- Password strength checker
- Password generator

## 👩‍💻 Author

**Ankita Katkar**

Python Developer | Computer Science Graduate

GitHub: https://github.com/ankitakatkar2024
