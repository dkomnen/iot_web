from services.BaseService import BaseService
from models.VikingModel import Viking
import time


class VikingService(BaseService):
    def __init__(self):
        super(VikingService, self).__init__()
        self.model = Viking

    def get_all(self):
        response = []
        data = []
        # print self.model.objects.all()

        return self.model.objects.all()

    def get_average_data(self, viking):
        data_sum = 0
        counter = 0
        for data in viking.temperature:
            counter += 1
            print data
            data_sum += data['sensor_reading']
        return data_sum / counter

    def get_graph_data(self, device_ids):
        data = {}
        epochTime = time.time()
        for device_id in device_ids:
            data[device_id] = []
            # device_data_array = self.model.objects(serial_number=device_id).batch_size(10000)
            # device_data_array = self.model.objects.aggregate({"$match": {"serial_number": device_id}, "$find": {"timestamp":{"$gte": searchStartTime, "$lt": searchEndTime}}})
            i = 1
            while i < 10:
                print "WE ARE IN THE LOOP NOW"
                searchStartTime = epochTime - i * 36000
                searchEndTime = epochTime - (i - 1) * 36000
                x = self.model.objects.aggregate({"$match": {"serial_number": device_id,
                                                             "timestamp": {"$gte": searchStartTime,
                                                                           "$lt": searchEndTime}}})

                # x = device_data_array.aggregate({"$find": {"timestamp":{"$gte": searchStartTime, "$lt": searchEndTime}}})
                counter = 0
                result_data = 0
                for device_data in x:
                    result_data += device_data['sensor_reading']
                    counter += 1
                data[device_id].append(result_data / counter)
                i += 1



                # result_data = 0
                # for device_data in device_data_array:
                #     result_data += device_data['sensor_reading']
                # data[device_id] = result_data

        return data

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
