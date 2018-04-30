from services.BaseService import BaseService
from models.DeviceModel import Device
from models.UserModel import User


class DeviceService(BaseService):
    def __init__(self):
        super(DeviceService, self).__init__()
        self.model = Device

    def create(self, data):
        serial_number = data['serial_number']
        device_type = data['device_type']
        name = data['name']

        return self.model(serial_number=serial_number, name=name, device_type=device_type).save()

