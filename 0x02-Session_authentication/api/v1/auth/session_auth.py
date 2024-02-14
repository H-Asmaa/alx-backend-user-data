#!/usr/bin/env python3
"""
0x02-Session_authentication
"""
from api.v1.auth.basic_auth import Auth
import uuid


class SessionAuth(Auth):
    """A class where to practice session based authentication."""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """A method that creates a session ID for user_id."""
        if user_id and isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """A method that returns a user id based on a session id."""
        if session_id and isinstance(session_id, str):
            return SessionAuth.user_id_by_session_id.get(session_id)
