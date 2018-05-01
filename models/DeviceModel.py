from mongoengine import *


class Device(Document):
    name = StringField(max_length=80)
    serial_number = StringField(max_length=80)
    device_type = StringField(max_length=100)
    status = StringField(max_length=100)
