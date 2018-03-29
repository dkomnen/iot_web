from bson import json_util


class BaseService(object):
    def __init__(self):
        self.model = None
        self.not_found_exception = None

    def get_by_id(self, resource_id):
        return self.model.objects(pk=resource_id)[0]

    def get_all(self):
        response = []

        for viking in self.model.objects.paginate(page=1, per_page=10).items:
            # viking.timestamp = datetime.datetime.fromtimestamp(viking.timestamp).strftime('%c')
            response.append(json_util.dumps(vars(viking)))
        return response
        # return self.model.objects.all()
