from pickle import TRUE
from flask import Blueprint, jsonify
from sqlalchemy import true
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