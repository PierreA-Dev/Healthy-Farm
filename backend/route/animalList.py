from flask import Blueprint, jsonify, request, abort
from app import Animal, Data
from flask_cors import cross_origin
from playhouse.shortcuts import model_to_dict

AnimalList_api = Blueprint('AnimalList_api', __name__)

@AnimalList_api.route("/liste_des_animaux")
@cross_origin()
def animal_list():
    """ Renvoie la liste des animaux """

    query = Data.select().group_by(Data.id_animal)
    list_animals=[]
    for data in query :

            d= model_to_dict(data)
            if data.temperature < 41 or data.temperature > 43 or data.heart_rate > 170 or data.heart_rate < 150:
                is_sick = True
            else:
                is_sick = False
            d['is_sick'] = is_sick
            list_animals.append(d)


    return jsonify(list_animals)

@AnimalList_api.route("/mon_animal")
@cross_origin()
def get_animal():
    """ Renvoie la page d'un animal """
    id=1
    # id = request.args.get('animal_id')

    try:
        id= Animal.get(Animal.id == id)
    except Exception:
        return abort(404)

    temperature_moy = 0
    heart_rate_moy = 0

    all = Data.select().where(Data.id_animal == id)
    query = Data.select().where(Data.id_animal == id).order_by(Data.id.desc()).get()
    list =[]

    if query.temperature < 41 or query.temperature > 43 or query.heart_rate > 170 or query.heart_rate < 150:
        is_sick = True
    else:
        is_sick = False
    
    dict = model_to_dict(query)
    dict['is_sick'] = is_sick
    list.append(dict)
    
    for d in all:
        temperature_moy += d.temperature
        heart_rate_moy += d.heart_rate

    list.append(temperature_moy/ len(all))
    list.append(heart_rate_moy/ len(all))

    return jsonify(list)