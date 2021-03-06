from services.BaseService import BaseService
from models.VikingModel import Viking
from models.DeviceModel import Device
from models.DeviceStatusModel import DeviceStatus
from utils.constants import graph_data_intervals
import time
import collections
import math


class VikingService(BaseService):
    def __init__(self):
        super(VikingService, self).__init__()
        self.model = Viking

    def get_all(self):
        return self.model.objects.all()

    def get_average_data(self, viking):
        data_sum = 0
        counter = 0
        for data in viking.temperature:
            counter += 1
            print data
            data_sum += data['sensor_reading']
        return data_sum / counter

    def get_graph_data(self, device_ids, interval, user_id):
        data = {}
        epoch_time = time.time()
        interval_seconds = graph_data_intervals.get(interval, 3600)
        for device_id in device_ids:
            device_name = Device.objects(serial_number=device_id)[0].name
            data[device_name] = collections.OrderedDict()
            i = 1
            while i < 10:
                search_start_time = epoch_time - i * interval_seconds
                search_end_time = epoch_time - (i - 1) * interval_seconds
                x = self.model.objects.aggregate({"$match": {"serial_number": device_id,
                                                             "timestamp": {"$gte": search_start_time,
                                                                           "$lt": search_end_time}}})

                counter = 0
                result_data = 0
                for device_data in x:
                    result_data += device_data['sensor_reading']
                    counter += 1
                if counter > 0:
                    data[device_name][search_end_time] = '%.3f' % (result_data / counter)
                else:
                    data[device_name][search_end_time] = 0
                i += 1
        for key, value in data.items():
            data[key] = collections.OrderedDict(reversed(data[key].items()))

        return data

    def get_devices_status(self):
        devices_status = DeviceStatus.objects.all()
        resp = []
        for device_status in devices_status:
            resp.append({"serial_number": device_status.serial_number, "status": device_status.status})
        return resp

    def create(self, data):
        serial_number = data['serial_number']
        sensor_reading = data['sensor_reading']
        sensor_type = data['sensor_type']
        unit = data['unit']
        timestamp = data['timestamp']

        return self.model(serial_number=serial_number, sensor_reading=sensor_reading, sensor_type=sensor_type,
                          unit=unit,
                          timestamp=timestamp).save()

    def dump_json(self, viking):
        result = {
            "serial_number": viking.serial_number,
            "start_timestamp": viking.start_timestamp,
            "end_timestamp": viking.end_timestamp,
            "unit": viking.unit,
            "temperature": viking.temperature
        }
        return result

    def dump_json_array(self, viking_array):
        result = []
        for viking in viking_array:
            result.append(self.dump_json(viking))

        return result
