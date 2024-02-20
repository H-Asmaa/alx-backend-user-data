#!/usr/bin/env python3
"""
0x03-user_authentication_service
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """A method that returns the hash of a password."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """A method that registers a user."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashedPw = _hash_password(password)
            user = self._db.add_user(email, hashedPw)
            return user
