from flask import request

from resources.BaseResource import BaseResource
from services.DeviceService import DeviceService
from services.UserService import UserService
from utils.response_handler import response_handler


class DeviceResource(BaseResource):
    def __init__(self):
        super(DeviceResource, self).__init__()
        self.resource_service = DeviceService()

    def get(self, resource_id=None):
        return response_handler.success(response_data=self.resource_service.get_all())

    def post(self):
        request_data = request.json
        for data in request_data['data']:
            self.resource_service.create(data)
        return response_handler.success()


class UserDeviceResource(BaseResource):
    def __init__(self):
        super(UserDeviceResource, self).__init__()
        self.resource_service = DeviceService()

    def get(self, resource_id=None):
        return response_handler.success(response_data=self.resource_service.get_all())

    def post(self, user_id, device_id=None):
        request_data = request.json

        user = UserService().get_by_id(resource_id=user_id)

        if device_id:
            device = self.resource_service.update(device_id, request_data)
        else:
            device = self.resource_service.create(request_data)
        user.update(add_to_set__devices=device, upsert=True)
        user.save()

        return response_handler.success(response_data=device.to_json())


class DeviceRemoteControlResource(BaseResource):
    def __init__(self):
        super(DeviceRemoteControlResource, self).__init__()
        self.resource_service = DeviceService()

    def post(self, status, device_id):
        self.resource_service.remote_control_device(device_id=device_id, status=status)

        return response_handler.success("Success")
