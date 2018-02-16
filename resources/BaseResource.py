from flask_restful import Resource
from utils.response_handler import response_handler


class BaseResource(Resource):

    def __init__(self):
        self.resource_service = None

    def get(self, resource_id=None):
        #try:
            if resource_id:
                return self.resource_service.get_by_id(resource_id, True)
            else:
                return self.resource_service.get_all()

        # except self.resource_service.not_found_exception as e:
        #     return response_handler.not_found(e.message)
        #
        # except Exception as e:
        #     return response_handler.bad_gateway(e.message)

