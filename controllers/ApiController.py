from server import api
from resources.VikingResource import VikingResource

api.add_resource(VikingResource, '/test')
