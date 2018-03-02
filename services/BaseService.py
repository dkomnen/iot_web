import json

class BaseService(object):

    def __init__(self):
        self.model = None
        self.not_found_exception = None

    def get_by_id(self, resource_id):
        pass

    def get_all(self):
        return self.model.objects.to_json()

