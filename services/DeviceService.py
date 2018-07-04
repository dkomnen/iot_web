from services.BaseService import BaseService
from models.DeviceModel import Device
from models.DeviceStatusModel import DeviceStatus
from mqtt.MqttClient import client


class DeviceService(BaseService):
    def __init__(self):
        super(DeviceService, self).__init__()
        self.model = Device

    def create(self, data):
        serial_number = data['serial_number']
        device_type = data['device_type']
        name = data['name']
        status = "down"

        return self.model(serial_number=serial_number, name=name, device_type=device_type, status=status).save()

    def update(self, device_id, data):
        serial_number = data['serial_number']
        device_type = data['device_type']
        name = data['name']

        device = self.get_by_id(device_id)
        device.update(serial_number=serial_number, name=name, device_type=device_type)
        return device

    def remote_control_device(self, device_id, status):
        device = DeviceStatus.objects(serial_number=device_id).first()
        if device.status is True:
            print "PUBLISHING TO TOPIC " + device_id + "/remote_shutdown"
            client.publish(device_id + "/remote_shutdown", "remote_control")
        elif device.status is False:
            print "PUBLISHING TO TOPIC " + device_id + "/remote_poweron"
            client.publish(device_id + "/remote_poweron", "remote_control")
