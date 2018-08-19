from flask_restful import Resource


class BaseResource(Resource):
    def __init__(self):
        self.resource_service = None

    def get(self, resource_id=None):
        if resource_id:
            return self.resource_service.get_by_id(resource_id, True)
        else:
            return self.resource_service.get_all()
