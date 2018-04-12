from flask import request

from resources.BaseResource import BaseResource
from services.VikingService import VikingService
from utils.response_handler import response_handler


class VikingResource(BaseResource):
    def __init__(self):
        super(VikingResource, self).__init__()
        self.resource_service = VikingService()

    def get(self, resource_id=None):
        return response_handler.success(self.resource_service.get_all())

    def post(self):
        request_data = request.json
        return response_handler.success(self.resource_service.create(request_data))


class VikingGraphResource(BaseResource):
    def __init__(self):
        super(VikingGraphResource, self).__init__()
        self.resource_service = VikingService()

    def post(self, resource_id=None):
        request_data = request.json
        device_ids = request_data['device_ids']

        return response_handler.success(self.resource_service.get_graph_data(device_ids=device_ids))
