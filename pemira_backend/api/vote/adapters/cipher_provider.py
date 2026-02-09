import base64
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from pemira_backend import settings
from pemira_backend.core.vote.ports.cipher_provider import ICipherProvider


class CipherProvider(ICipherProvider):
    def __init__(self):
        self.encryption_key = settings.APP_ENCRYPTION_KEY.encode("utf-8")
        self.padding = padding.PKCS7(128)

    def encrypt(self, text: str) -> str:
        iv = os.urandom(16)

        padder = self.padding.padder()
        padded_data = padder.update(text.encode("utf-8")) + padder.finalize()

        cipher = Cipher(algorithms.AES(self.encryption_key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return f"{base64.b64encode(iv).decode('utf-8')}$${base64.b64encode(ciphertext).decode('utf-8')}"


    def decrypt(self, text: str) -> str:
        parts = text.split('$$')
        iv = base64.b64decode(parts[0])
        ciphertext = base64.b64decode(parts[1])

        cipher = Cipher(algorithms.AES(self.encryption_key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = self.padding.unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

        return unpadded_data.decode("utf-8")