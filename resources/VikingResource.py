from flask import request

from resources.BaseResource import BaseResource
from services.VikingService import VikingService
from utils.response_handler import response_handler


class VikingResource(BaseResource):

    def __init__(self):
        super(VikingResource, self).__init__()
        self.resource_service = VikingService()

    def get(self, resource_id=None):
        return response_handler.success(response_data=self.resource_service.get_all())

    def post(self):
        request_data = request.get_json()
        return response_handler.success(respone_data=self.resource_service.create(request_data))