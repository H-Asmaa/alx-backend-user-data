#!/usr/bin/env python3
"""
0x01. Basic authentication
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """A class that inherits from Auth."""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """A method that returns the Base64 of the Authorization header."""
        return (
            authorization_header[6:]
            if authorization_header is not None
            and isinstance(authorization_header, str)
            and authorization_header.startswith("Basic ")
            else None
        )

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """A method that returns the decoded value of base64."""
        if base64_authorization_header is not None and isinstance(
                base64_authorization_header, str):
            try:
                decodedBytes = base64.b64decode(base64_authorization_header)
                return decodedBytes.decode('utf-8')
            except base64.binascii.Error:
                return None
        return None
