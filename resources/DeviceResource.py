from flask import request

from resources.BaseResource import BaseResource
from services.DeviceService import DeviceService
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

    def post(self):
        request_data = request.json
        for data in request_data['data']:
            self.resource_service.create(data)
        return response_handler.success()
