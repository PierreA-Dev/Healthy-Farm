from asyncio.windows_events import NULL
from flask import Blueprint, jsonify, request
from app import Animal, Data
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

    temperature_moy = NULL
    heart_rate_moy = NULL

    all = Data.select().where(Data.id_animal == id)
    query = Data.select().where(Data.id_animal == id).order_by(Data.id.desc()).get()
    list =[]

    if query.temperature < 41 or query.temperature > 43 or query.heart_rate > 170:
        is_sick = True
    else:
        is_sick = False
    
    list.append(model_to_dict(query))
    list.append(is_sick)
    
    for d in all:
        temperature_moy += d.temperature
        heart_rate_moy += d.heart_rate

    list.append(temperature_moy/ len(all))
    list.append(heart_rate_moy/ len(all))

    return jsonify(list)