#!/usr/bin/env python3
"""
0x02-Session_authentication
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """A new authentication class."""

    def create_session(self, user_id=None):
        """A method that creates and stores new instance
        of UserSession and returns the Session ID"""
        new_session = super().create_session(user_id)
        if isinstance(new_session, str):
            user_session = UserSession(user_id=user_id, session_id=new_session)
            user_session.save()
            return new_session
        return None

    def user_id_for_session_id(self, session_id=None):
        """A method that returns the User ID by requesting
        UserSession in the database based on session_id"""
        if session_id and isinstance(session_id, str):
            userSession = UserSession().search({"session_id": session_id})
            return userSession[0].user_id if len(userSession) > 0 else None
        return None

    def destroy_session(self, request=None):
        """A method that destroys the UserSession based on the
        Session ID from the request cookie"""
        session_id = self.session_cookie(request)
        userSession = UserSession().search({"session_id": session_id})
        if len(userSession):
            userSession[0].delete()
            return True
        return False
