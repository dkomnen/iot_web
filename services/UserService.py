from services.BaseService import BaseService
from models.UserModel import User
from models.DeviceModel import Device


class UserService(BaseService):
    def __init__(self):
        super(UserService, self).__init__()
        self.model = User

    def get_devices_by_user_id(self, user_id):
        user = self.get_by_id(user_id)
        return user.devices

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


