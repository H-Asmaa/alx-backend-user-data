#!/usr/bin/env python3
"""
0x00-personal_data
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """A function that hashes a password that is passed as string."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
