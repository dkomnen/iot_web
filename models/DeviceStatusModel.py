from mongoengine import *


class DeviceStatus(Document):
    name = StringField(max_length=80)
    serial_number = StringField(max_length=80)
    status = BooleanField(default=False)

    meta = {"collection": "device_status"}
