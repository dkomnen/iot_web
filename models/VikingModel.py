from BaseModel import BaseModel
from mongoengine import *
from config.Config import Config


class Viking(DynamicDocument):

    #collection_name = "viking"
    payload = StringField()
    meta = {"collection": "viking"}

    # def __init__(self):
    #     super(Viking, self).__init__()

