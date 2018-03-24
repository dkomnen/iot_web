from server import api
from resources.VikingResource import VikingResource
from resources.DeviceResource import DeviceResource, UserDeviceResource

api.add_resource(VikingResource, '/api/viking')
api.add_resource(UserDeviceResource, '/api/user/<string:user_id>/device')
