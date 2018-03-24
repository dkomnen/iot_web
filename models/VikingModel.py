from BaseModel import BaseModel
from flask_mongoengine import MongoEngine
#from server import db

db = MongoEngine()

class Viking(db.DynamicDocument):

    #collection_name = "viking"
    payload = db.StringField()
    meta = {"collection": "viking"}


