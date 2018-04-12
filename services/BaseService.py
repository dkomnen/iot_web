from bson import json_util
from pymongo import MongoClient


class BaseService(object):
    def __init__(self):
        self.model = None
        self.not_found_exception = None

    def get_by_id(self, resource_id):
        return self.model.objects(pk=resource_id)[0]

    def get_all(self):
        return self.model.objects.all()

    def dump_json(self, data):
        pass

    def dump_json_array(self, data_array):
        pass
