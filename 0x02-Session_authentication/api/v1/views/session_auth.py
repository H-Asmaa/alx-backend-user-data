#!/usr/bin/env python3
""" Module of session views
"""
from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def user_session() -> str:
    """POST /api/v1/auth_session/login
    Return:
      - A route for the user authentication.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    user = user[0]
    if not user.is_valid_password(str(password)):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    session_name = getenv("SESSION_NAME")
    response = jsonify(user.to_json())
    response.set_cookie(session_name, session_id)
    return response
