import os
import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Legacy values retained only for backward compatibility with old-format encrypted passwords.
# New encryptions use random IVs and require the ENCRYPTION_KEY env var.
_LEGACY_IV = b'0123456789abcdef'
_LEGACY_KEY = "1234567890abcdef123456"


def _get_key() -> bytes:
    secret_key = os.environ.get("ENCRYPTION_KEY", _LEGACY_KEY)
    key_bytes = secret_key.encode('utf-8')
    if len(key_bytes) != 24:
        key_bytes = key_bytes.ljust(24, b'\0')[:24]
    return key_bytes


def _is_legacy_format(raw_bytes: bytes) -> bool:
    """Detect if data was encrypted with the old fixed-IV scheme."""
    return len(raw_bytes) <= 32


def encrypt(raw_text: str) -> str:
    key_bytes = _get_key()
    iv_bytes = os.urandom(16)

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(raw_text.encode('utf-8')) + padder.finalize()

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv_bytes), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    return binascii.hexlify(iv_bytes + encrypted).decode('utf-8')


def decrypt(enc_text: str) -> str:
    key_bytes = _get_key()
    raw_bytes = binascii.unhexlify(enc_text.encode('utf-8'))

    if _is_legacy_format(raw_bytes):
        iv_bytes = _LEGACY_IV
        encrypted_bytes = raw_bytes
    else:
        iv_bytes = raw_bytes[:16]
        encrypted_bytes = raw_bytes[16:]

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv_bytes), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_bytes) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(padded_data) + unpadder.finalize()

    return decrypted_data.decode('utf-8')


if __name__ == "__main__":
    sample_text = "password123"
    encrypted = encrypt(sample_text)
    print(f"Encrypted: {encrypted}")
    decrypted = decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
    print(encrypt("SuperSecretPassword!"))
