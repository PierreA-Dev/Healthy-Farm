from flask import Blueprint, jsonify, request
from app import Animal
from flask_cors import cross_origin
from playhouse.shortcuts import model_to_dict

AnimalList_api = Blueprint('AnimalList_api', __name__)

@AnimalList_api.route("/liste_des_animaux")
@cross_origin()
def animal_list():
    """ Renvoie la liste des animaux """

    query = Animal.select()
    list=[]
    """query.to_dict()"""
    for data in query :
        d= model_to_dict(data)
        list.append(d)

    return jsonify(list)

@AnimalList_api.route("/mon_animal")
@cross_origin()
def get_animal():
    """ Renvoie la page d'un animal """
    id=1
    # id = request.args.get('animal_id')

    query = Animal.select().where(Animal.id == id).get()

    print(jsonify(model_to_dict(query)))

    return jsonify(model_to_dict(query))