#!/usr/bin/env python3
"""
0x01. Basic authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """A class where to practice authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A method that checks if authentication is required for a path."""
        if path and not path.endswith(('/')):
            path = path + '/'
        return not path or not excluded_paths or path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """A method that extract header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """A method that gets the user from the request."""
        return None
