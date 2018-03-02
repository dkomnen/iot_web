from mongoengine import *


class UserModel(DynamicDocument):

    meta = {"collection": "user"}

