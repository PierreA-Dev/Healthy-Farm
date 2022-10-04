from flask import Blueprint, redirect, url_for
from flask_login import logout_user

login_api = Blueprint('login_api', __name__)


@login_api.route("/login")
def login():
    """ Renvoie la page de login"""
    return "page de login"


@login_api.route("/logout")
def logout():
    """ Déconnecter le user """
    logout_user()
    return redirect(url_for('login_api.login'))

