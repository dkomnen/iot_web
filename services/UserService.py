from services.BaseService import BaseService
from models.UserModel import User
from models.DeviceModel import Device
from models.DeviceStatusModel import DeviceStatus


class UserService(BaseService):
    def __init__(self):
        super(UserService, self).__init__()
        self.model = User

    def get_devices_by_user_id(self, user_id):
        user = self.get_by_id(user_id)
        devices = user.devices
        for device in devices:
            device_status = DeviceStatus.objects(serial_number=device.serial_number).first()
            if device_status is not None:
                device.status = device_status.status

        return devices

    def get_device_by_user_id_and_type(self, user_id, device_type):
        devices = self.model.objects(id=user_id).devices

    def get_by_user_id_and_type(self, user_id, device_type):
        #devices = Device.objects(device_type=device_type, user__in=(self.model.objects.filter(id=user_id).all()))
        devices = self.get_by_id(resource_id=user_id).devices
        result = []
        for device in devices:
            if device.device_type == device_type:
                result.append(device)
        print result
        return result


