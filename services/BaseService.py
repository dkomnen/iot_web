from bson import json_util
from pymongo import MongoClient


class BaseService(object):
    def __init__(self):
        self.model = None
        self.not_found_exception = None

    def get_by_id(self, resource_id):
        return self.model.objects(pk=resource_id)[0]

    def get_all(self):
        response = []

        # for viking in self.model.objects.paginate(page=1, per_page=10).items:
        #     # viking.timestamp = datetime.datetime.fromtimestamp(viking.timestamp).strftime('%c')
        #     response.append(json_util.dumps(vars(viking)))
        # return response
        #return self.dump_json_array(self.model.objects.paginate(page=1, per_page=1000).items)
        #return self.dump_json_array(self.model.objects.all())
        # return self.model.objects.all()
        client = MongoClient("localhost", 27017, maxPoolSize=100)
        db = client.heimdall
        collection = db['viking']
        cursor = collection.find({}).batch_size(5000000)
        print cursor
        print self.model.objects.all()

        return self.dump_json_array(self.model.objects.all())

    def dump_json(self, data):
        pass

    def dump_json_array(self, data_array):
        pass
