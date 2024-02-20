#!/usr/bin/env python3
"""
0x03-user_authentication_service
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """A method that returns the hash of a password."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
