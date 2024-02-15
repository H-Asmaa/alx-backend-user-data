#!/usr/bin/env python3
"""
0x02-Session_authentication
"""
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """A new authentication class."""

    def create_session(self, user_id=None):
        """A method that creates and stores new instance
        of UserSession and returns the Session ID"""
        pass

    def user_id_for_session_id(self, session_id=None):
        """A method that returns the User ID by requesting
        UserSession in the database based on session_id"""
        pass

    def destroy_session(self, request=None):
        """A method that destroys the UserSession based on the
        Session ID from the request cookie"""
        pass
