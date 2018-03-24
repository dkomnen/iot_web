from bson import json_util
import datetime

class BaseService(object):

    def __init__(self):
        self.model = None
        self.not_found_exception = None

    def get_by_id(self, resource_id):
        pass

    def get_all(self):
        print "HI"
        #print self.model.objects.to_json()
        response = []

        for viking in self.model.objects.paginate(page=1, per_page=10).items:
            #viking.timestamp = datetime.datetime.fromtimestamp(viking.timestamp).strftime('%c')
            response.append(json_util.dumps(vars(viking)))
        print json_util.dumps(response[0])
        print json_util._json_convert(response[0])
        return response
        #return self.model.objects.all()

