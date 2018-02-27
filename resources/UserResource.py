from flask import request

from resources.BaseResource import BaseResource
from services.UserService import UserService
from utils.response_handler import response_handler


class UserResource(BaseResource):

    def __init__(self):
        super(UserResource, self).__init__()
        self.resource_service = UserService()

    # def post(self):
    #     request_data = request.get_json()
    #     return response_handler.success(respone_data=self.resource_service.create(request_data))