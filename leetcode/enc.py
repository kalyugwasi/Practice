"""
def encrypt(word: str, key: int):
    return "".join(chr(ord(ch) ^ key) for ch in word)
msg = "Hello World"
key = 78
print(msg)
cipher = encrypt(msg, key)
print(cipher)
des = encrypt(cipher,key)
print(des)
"""
import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 256-bit key from a password."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def encrypt(plaintext: str, password: str) -> str:
    """Encrypt plaintext and return base64-encoded ciphertext."""
    salt = os.urandom(16)
    nonce = os.urandom(12)

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)

    payload = salt + nonce + ciphertext
    return base64.b64encode(payload).decode()


def decrypt(ciphertext_b64: str, password: str) -> str:
    """Decrypt base64-encoded ciphertext."""
    payload = base64.b64decode(ciphertext_b64)

    salt = payload[:16]
    nonce = payload[16:28]
    ciphertext = payload[28:]

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext.decode()

message = "Hello World"
password = "super-secure-password"

encrypted = encrypt(message, password)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, password)
print("Decrypted:", decrypted)
