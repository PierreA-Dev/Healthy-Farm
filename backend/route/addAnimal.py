from flask import Blueprint

addAnimal_api = Blueprint('addAnimal_api', __name__)

@addAnimal_api.route("/ajouter_un_animal")
def addAnimal():
    """ Ajouter un animal """

    return "<p>page d'ajout</p>"