
from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    """Create a key file if it doesn't exist (run once)."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

def load_key():
    """Load the encryption key from disk."""
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_text(plain_text: str) -> str:
    """Encrypt a string and return a safe text version for SQLite."""
    if plain_text is None:
        return None
    f = Fernet(load_key())
    return f.encrypt(plain_text.encode("utf-8")).decode("utf-8")

def decrypt_text(cipher_text: str) -> str:
    """Decrypt a string from SQLite and return readable text."""
    if cipher_text is None:
        return None
    f = Fernet(load_key())
    return f.decrypt(cipher_text.encode("utf-8")).decode("utf-8")
