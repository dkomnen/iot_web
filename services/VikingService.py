from services.BaseService import BaseService
from models.VikingModel import Viking


class VikingService(BaseService):
    def __init__(self):
        super(VikingService, self).__init__()
        self.model = Viking

    def get_all(self):
        response = []
        data = []
        for viking in self.model.objects.all():
            data.append(self.get_average_data(viking))
        print self.model.objects.all()

        return data

    def get_average_data(self, viking):
        data_sum = 0
        counter = 0
        for data in viking.temperature:
            counter += 1
            print data
            data_sum += data['temperature']
        return data_sum / counter

    def create(self, data):
        serial_number = data['serial_number']
        temperature = data['temperature']
        unit = data['unit']
        start_timestamp = data['start_timestamp']
        end_timestamp = data['end_timestamp']

        # return self.model(payload=unit).save().to_json()
        return self.model(serial_number=serial_number, temperature=temperature, unit=unit,
                          start_timestamp=start_timestamp, end_timestamp=end_timestamp).save()

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
