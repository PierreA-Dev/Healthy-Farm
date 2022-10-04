from flask import Blueprint

index_api = Blueprint('index_api', __name__)

@index_api.route("/")
def index():
    """ Renvoie la page d'accueil """
    return "<p>Hello, World!</p>"