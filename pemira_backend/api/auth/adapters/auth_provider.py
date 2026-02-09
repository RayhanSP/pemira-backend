import binascii
import os

from pemira_backend.core.auth.ports.auth_provider import IAuthProvider


class AuthProvider(IAuthProvider):
    def generate_token(self) -> str:
        return binascii.hexlify(os.urandom(20)).decode()
