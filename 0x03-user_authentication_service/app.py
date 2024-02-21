#!/usr/bin/env python3
"""
0x03-user_authentication_service
"""
from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def index():
    """The index method."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def user():
    """A function that implements the POST /users route."""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        AUTH.register_user(email=email, password=password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """A function that takes care of the login."""
    email = request.form.get("email")
    password = request.form.get("password")
    if email and password:
        validation = AUTH.valid_login(email=email, password=password)
        if not validation:
            abort(401)
        session_id = AUTH.create_session(email=email)
        response = jsonify({"email": f"{email}", "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response


@app.route("/sessions", methods=["DELETE"])
def logout():
    """A function that takes care of the logout."""
    session_id = request.cookies.get("session_id")
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect(url_for("index"))
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
