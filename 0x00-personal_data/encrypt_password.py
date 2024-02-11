#!/usr/bin/env python3
"""
0x00-personal_data
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """A function that hashes a password that is passed as string."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """A function that validates if the encrypt is associated
    to a password."""
    return (
        True
        if bcrypt.checkpw(password.encode(), hashed_password)
        else False
    )
