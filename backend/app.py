from datetime import datetime
from flask import Flask
from playhouse.flask_utils import FlaskDB
from peewee import *
import click


app = Flask(__name__)
DATABASE = 'sqlite:///healthyfarm.db'
SECRET_KEY = 'secret_key'

app = Flask(__name__)
app.config.from_object(__name__)
db_wrapper = FlaskDB(app)


# definition des classes
class User(db_wrapper.Model):
    email = CharField(unique=True)
    password = CharField()
    is_admin = BooleanField(default=False)
    role = CharField()

class Building(db_wrapper.Model):
    name = CharField(unique=True)
    zone = CharField()

class Animal(db_wrapper.Model):
    email = CharField(unique=True)
    number = FloatField()
    arrived = DateTimeField(default=datetime.now)
    left = DateTimeField()

class Data(db_wrapper.Model):
    temperature = FloatField()
    heart_rate = FloatField()
    lat = FloatField()
    long = FloatField()
    id_animal = ForeignKeyField(Animal, backref='animal')


# login_manager.init_app(app)
# login_manager.login_view = "login_api.login"

#Import des blueprints
from route.index import index_api


app.register_blueprint(index_api)

@app.cli.command("init_db")
def init_db():
    """Cette commande initialise la BDD """

    try:
        with db_wrapper.database:
            db_wrapper.database.create_tables([User, Building, Animal, Data])

        email = click.prompt('Your email address', type=str)
        password = click.prompt('Your password', type=str, hide_input=True)

        User.create(email=email, password=password, is_admin=True, role = "exploitant")

    except Exception:
        click.echo('Une erreur s\'est produite.')
        exit(1)

    else:
        click.echo('Base de données correctement initialisée.')
        exit(0)