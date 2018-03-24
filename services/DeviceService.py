from services.BaseService import BaseService
from models.DeviceModel import Device


class DeviceService(BaseService):
    def __init__(self):
        super(DeviceService, self).__init__()
        self.model = Device

    def create(self, data):
        serial_number = data['serial_number']
        name = data['name']

        return self.model(serial_number=serial_number, name=name).save().to_json()
