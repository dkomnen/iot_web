from mongoengine import *


class Device(EmbeddedDocument):
    name = StringField(max_length=80)
    serial_number = StringField(max_length=80, unique=True)