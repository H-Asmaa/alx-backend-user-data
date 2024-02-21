#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

session_id = auth.create_session(email)
print(session_id)
auth.update_password(auth.get_reset_password_token(email), "password")
print(auth.valid_login(email, "password"))
