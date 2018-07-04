from server import api
from resources.VikingResource import VikingResource, VikingGraphResource, VikingStatus
from resources.DeviceResource import DeviceResource, UserDeviceResource, DeviceRemoteControlResource

api.add_resource(VikingResource, '/api/viking')
api.add_resource(VikingGraphResource, '/api/viking/graph_data')
api.add_resource(VikingStatus, '/api/viking/status')
api.add_resource(UserDeviceResource, '/api/user/<string:user_id>/device/<string:device_id>',
                 '/api/user/<string:user_id>/device')
api.add_resource(DeviceRemoteControlResource, '/api/device/<string:device_id>/<string:status>')
