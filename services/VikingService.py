from services.BaseService import BaseService
from models.VikingModel import Viking


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
            data_sum += data['temperature']
        return data_sum / counter

    def get_graph_data(self, device_ids):
        data = {}
        for device_id in device_ids:
            #device_data_array = self.model.objects(serial_number=device_id).batch_size(10000)
            device_data_array = self.model.objects.aggregate({"$match": {"serial_number": device_id}})
            result_data = 0
            for device_data in device_data_array:
                result_data += device_data['temperature']
            data[device_id] = result_data

        return data

    def create(self, data):
        serial_number = data['serial_number']
        temperature = data['temperature']
        unit = data['unit']
        timestamp = data['timestamp']

        return self.model(serial_number=serial_number, temperature=temperature, unit=unit,
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
