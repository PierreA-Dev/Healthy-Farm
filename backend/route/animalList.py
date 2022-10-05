from flask import Blueprint, jsonify
from app import Animal
from flask_cors import cross_origin

AnimalList_api = Blueprint('AnimalList_api', __name__)

@AnimalList_api.route("/liste_des_animaux")
@cross_origin()
def animal_list():
    """ Renvoie la liste des animaux """

    query = Animal.select()
    list=[]
    for q in query:
        list = list.append(q)

    return jsonify(list)