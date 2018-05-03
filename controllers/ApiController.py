from server import api
from resources.VikingResource import VikingResource, VikingGraphResource
from resources.DeviceResource import DeviceResource, UserDeviceResource

api.add_resource(VikingResource, '/api/viking')
api.add_resource(VikingGraphResource, '/api/viking/graph_data')
api.add_resource(UserDeviceResource, '/api/user/<string:user_id>/device/<string:device_id>')
