from mongoengine import *
from models.RoleModel import Role
from models.DeviceModel import Device


class User(Document):

    email = StringField(max_length=255)
    password = StringField(max_length=255)
    active = BooleanField(default=True)
    #confirmed_at = db.DateTimeField()
    roles = ListField(ReferenceField(Role), default=[])
    devices = ListField(ReferenceField(Device), default=[])

    meta = {"collection": "user"}

